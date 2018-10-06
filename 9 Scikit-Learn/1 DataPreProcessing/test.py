from sklearn import preprocessing
import numpy as np

X_origin = np.array([[1., -1., 2.],
                     [2., 0., 0.],
                     [0., 1., -1.]])

min_max_scaler = preprocessing.MinMaxScaler([0, 4])
X_train_minmax = min_max_scaler.fit_transform(X_origin)
print(X_train_minmax)

X_transform = min_max_scaler.transform(X_origin)
print(X_transform)

X_trans_origin = min_max_scaler.inverse_transform(X_transform)

print(X_trans_origin)

print(min_max_scaler.feature_range)

print(min_max_scaler.data_min_)
print(min_max_scaler.data_max_)
print(min_max_scaler.scale_)


