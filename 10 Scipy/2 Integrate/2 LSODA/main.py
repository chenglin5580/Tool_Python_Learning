
from Bennu import Bennu
import numpy as np
import matplotlib.pyplot as plt


def Interal_verify():
    lambda_0 = np.random.rand(1)
    lambda_n = np.random.rand(Object.lambda_dim) * 2 - 1
    costate_0 = np.hstack([lambda_0, lambda_n])

    observation, ceq, done, info = Object.Fun_GetTraFromCostate(costate_0)
    print(observation)


def Interal_verify2():
    # costate_0 = np.array([0.0162989,0.000618658,-0.000207789,3.66103e-005,0.814424,0.576953,0.0597774,5.70709e-007])
    costate_0 = np.array(
        [0.0141882, 0.00060483, -0.000189421, 3.65392e-005,  0.819257, 0.570103, 0.0599928, 5.64014e-007])
    observation, ceq, done, info = Object.Fun_GetTraFromCostate(costate_0)
    print(observation)
    print(observation[-1, :])
    print(ceq)

    plt.figure(1)
    plt.plot(observation[:, 6])

    plt.figure(2)
    plt.plot(info['u_seq'])

    plt.show()


def shooting():
    for i in range(1000):
        res, samples, done, info = Object.Fun_Optimize()
        print(i, done, res.fun)
        if done:
            print(res.x)
            break


if __name__ == '__main__':

    Object = Bennu()
    # 测试积分没有问题
    # Interal_verify()
    # Interal_verify2()

    # 打靶
    shooting()

