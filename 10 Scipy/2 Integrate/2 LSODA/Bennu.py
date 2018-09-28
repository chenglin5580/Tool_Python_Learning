
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import integrate
from scipy.optimize import root, minimize


class Bennu:

    def __init__(self, random=False):
        self.t = None
        self.state = None
        self.random = random
        # 对象参数设置
        self.omega = 4.061266439e-04
        self.r_f_T = np.array([0.22, 0.031, 0.1])
        self.v_f_T = np.array([0., 0., 0.])
        self.r_0 = np.array([0.72, 0.035, 0.12])
        self.v_0 = np.array([0.01/1000, 0.01/1000, 0.01/1000])
        self.m0 = np.array([800])

        self.Trust = 0.3 / 1000
        self.Isp = 3800
        self.tf = 2800
        self.g0 = 9.8 / 1000
        self.epsilon = 1

        # 仿真设置
        self.reset()
        self.state_dim, self.lambda_dim, self.control_dim = 7, 7, 3

    def render(self):
        pass

    def reset(self, observation_input=None):
        self.t = 0
        if observation_input is None:
            if self.random is not True:
                self.state = np.hstack((self.r_0, self.v_0, self.m0))
            else:
               pass
        else:
            self.state = observation_input

        self.observation = self.state.copy()
        return self.observation

    def Fun_Optimize(self, observation_input=None, costate_0=None):

        if observation_input is None:
            self.reset()
            lambda_0 = np.random.rand(1)
            lambda_n = np.random.rand(self.lambda_dim) * 2 - 1
            # lambda_0 = np.sqrt(1/(np.linalg.norm(lambda_n)**2 + 1))
            # lambda_n = lambda_n * lambda_0
            costate_0 = np.hstack([lambda_0, lambda_n])
            costate_0 = costate_0 / np.linalg.norm(costate_0)
            # costate_0 = np.array(
            #     [0.0141882, 0.00060483, -0.000189421, 3.65392e-005, 0.819257, 0.570103, 0.0599928, 5.64014e-007])
        else:
            self.reset(observation_input=observation_input)

        res = root(self.Fun_Shoot, costate_0, method='hybr', tol=1e-8, options={'factor': 0.1, 'band': None})
        # samples, ceq, done, info = self.Fun_GetSamples(res.x)
        done = True if np.linalg.norm(res.fun) < 1e-6 else False
        return res, [], done, []


    def Fun_Shoot(self, costate_0):
        observation, ceq, done, info = self.Fun_GetTraFromCostate(costate_0)
        return ceq


    def Fun_GetTraFromCostate(self, costate):

        self.lambda_0 = costate[0]
        lambda_0 = self.lambda_0
        lambda_n = costate[1:]

            # 微分方程
        X0 = np.hstack([self.state, lambda_n])
        # t = np.linspace(0, self.tf, 101)
        # X = odeint(self.motionEquation, X0, t, args=(lambda_0,), rtol=1e-8, atol=1e-8)
        # X = integrate.LSODA(self.motionEquation, t0=0, y0=X0, t_bound=self.tf)
        X = integrate.RK45(self.motionEquation, t0=0, y0=X0, t_bound=self.tf)
        while True:
            if X.t < self.tf:
                X.step()
            else:
                break
        Xf = X.y
        r = Xf[0:3]
        v = Xf[3:6]
        lambda_m = Xf[13]

        ceq = np.hstack((r-self.r_f_T, v-self.v_f_T, lambda_m, np.linalg.norm(costate)-1))
        done ={}
        info = {}
        return Xf, ceq, done, info


    def motionEquation(self, t, input):

        lambda_0 = self.lambda_0

        r = input[0:3]
        v = input[3:6]
        m = input[6]
        lambda_r = input[7:10]
        lambda_v = input[10:13]
        lambda_m = input[13]

        normLamV = np.linalg.norm(lambda_v)

        rho = 1 - self.Isp * self.g0 * normLamV / lambda_0 / m - lambda_m / lambda_0

        if rho > self.epsilon:
            u = 0
        elif rho < -self.epsilon:
            u = 1
        else:
            u = (self.epsilon - rho) / self.epsilon / 2

        # print(u)

        alpha = - lambda_v / normLamV

        state_dot = np.zeros(shape=14)
        state_dot[0:3] = v
        state_dot[3] =  2 * v[1] * self.omega + r[0] * self.omega * self.omega + self.Trust * u * alpha[0] / m
        state_dot[4] = -2 * v[0] * self.omega + r[1] * self.omega * self.omega + self.Trust * u * alpha[1] / m
        state_dot[5] = self.Trust * u * alpha[2] / m
        state_dot[6] = -self.Trust * u/self.Isp/self.g0
        state_dot[7] = lambda_v[0]*self.omega*self.omega
        state_dot[8] = lambda_v[1] * self.omega * self.omega
        state_dot[9] = 0
        state_dot[10] = -lambda_r[0] + 2 * lambda_v[1]*self.omega
        state_dot[11] = -lambda_r[1] - 2 * lambda_v[0] * self.omega
        state_dot[12] = -lambda_r[2]
        state_dot[13] = - self.Trust * u * normLamV / m / m
        return state_dot














