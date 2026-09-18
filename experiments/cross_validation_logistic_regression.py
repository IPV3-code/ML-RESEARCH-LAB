import numpy as np
import matplotlib.pyplot as plt
from algorithms.supervised.logistic_regression import LogisticRegression

mu_0, mu_1 = np.array([0, 0]), np.array([2, 2])
covariance = np.array([
    [1, 0],
    [0, 1]
])

class_0 = np.random.multivariate_normal(mu_0, covariance, 100)
class_1 = np.random.multivariate_normal(mu_1, covariance, 100)

y_0 = np.zeros(100)
y_1 = np.ones(100)

y_0 = y_0.reshape(-1, 1)
y_1 = y_1.reshape(-1, 1)

indices_0 = np.arange(0, 100)
indices_1 = np.arange(0, 100)

np.random.shuffle(indices_0)
np.random.shuffle(indices_1)

fold_0 = np.array_split(indices_0, 5)
fold_1 = np.array_split(indices_1, 5)

lambda_values = [0, 0.01, 0.1, 1]
validation_losses = []

for i in range(5):
    training_fold_0 = np.hstack(fold_0[0:i] + fold_0[i + 1:])
    training_fold_1 = np.hstack(fold_1[0:i] + fold_1[i + 1:])

    validation_0 = fold_0[i]
    validation_1 = fold_1[i]

    x_train_0 = class_0[training_fold_0]
    x_train_1 = class_1[training_fold_1]

    x_validation_0 = class_0[validation_0]
    x_validation_1 = class_1[validation_1]

    y_train_0 = y_0[training_fold_0]
    y_train_1 = y_1[training_fold_1]

    y_validation_0 = y_0[validation_0]
    y_validation_1 = y_1[validation_1]

    x_train = np.vstack((x_train_0, x_train_1))
    y_train = np.vstack((y_train_0, y_train_1))

    x_validation = np.vstack((x_validation_0, x_validation_1))
    y_validation = np.vstack((y_validation_0, y_validation_1))

    x_ones_column_train = np.ones((x_train.shape[0], 1))
    x_train = np.hstack((x_ones_column_train, x_train))

    x_ones_column_validation = np.ones((x_validation.shape[0], 1))
    x_validation = np.hstack((x_ones_column_validation, x_validation))

    for lambda_value in lambda_values:
        model = LogisticRegression(10000, 0.01, 1e-5, None, lambda_value)
        model.fit(x_train, y_train)

        h_validation = model.predict_proba(x_validation)
        validation_losses.append(model.compute_loss(
            h_validation, y_validation, model.theta, include_regularization=False))

validation_losses = np.reshape(validation_losses, (5, 4))
cv_losses = np.mean(validation_losses, axis=0)
# print(cv_losses.shape)
# print(cv_losses)

# min_validation_loss_index = np.argmin(cv_losses)
# print(
#     f'lambda with smallest cv loss : {lambda_values[min_validation_loss_index]}')

for lambda_value, cv_loss in zip(lambda_values, cv_losses):
    print(f'{lambda_value} : {cv_loss}')
