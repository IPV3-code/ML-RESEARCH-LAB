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

plt.scatter(class_0[:, 0], class_0[:, 1], marker='o', c='red', label='class 0')
plt.scatter(class_1[:, 0], class_1[:, 1],
            marker='x', c='black', label='class 1')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Class 0 vs Class 1')
plt.legend()
plt.show()

y_0 = np.zeros(100)
y_1 = np.ones(100)

y_0 = y_0.reshape(-1, 1)
y_1 = y_1.reshape(-1, 1)

indices_0 = np.arange(100)
indices_1 = np.arange(100)

np.random.shuffle(indices_0)
np.random.shuffle(indices_1)

training_indices_0, validation_indices_0 = indices_0[:80], indices_0[80:]
training_indices_1, validation_indices_1 = indices_1[:80], indices_1[80:]

x_0_train, y_0_train = class_0[training_indices_0], y_0[training_indices_0]
x_1_train, y_1_train = class_1[training_indices_1], y_1[training_indices_1]

x_0_validation, y_0_validation = class_0[validation_indices_0], y_0[validation_indices_0]
x_1_validation, y_1_validation = class_1[validation_indices_1], y_1[validation_indices_1]

x_train = np.vstack((x_0_train, x_1_train))
y_train = np.vstack((y_0_train, y_1_train))

x_validation = np.vstack((x_0_validation, x_1_validation))
y_validation = np.vstack((y_0_validation, y_1_validation))


lambda_values = [0, 0.01, 0.1, 1]

ones_column_x_train = np.ones((x_train.shape[0], 1))
x_train = np.hstack((ones_column_x_train, x_train))

ones_column_x_validation = np.ones((x_validation.shape[0], 1))
x_validation = np.hstack((ones_column_x_validation, x_validation))


models = []

for lambda_value in lambda_values:
    model = LogisticRegression(10000, 0.01, 1e-5, None, lambda_value)
    model.fit(x_train, y_train)
    models.append(model)

    print(f'{lambda_value} - {model.n_iterations} \n')
    print(f'{lambda_value} - {model.theta} \n')
    print(f'{lambda_value} - {model.loss_history[-1]} \n')

validation_losses = []
for model in models:
    h_validation = model.predict_proba(x_validation)
    loss = model.compute_loss(
        h_validation, y_validation, model.theta, include_regularization=False)
    validation_losses.append(loss)

    print(f'{model.lambda_reg} - {loss}')

training_losses = []
for model in models:
    training_losses.append(model.loss_history[-1])

x_train_min = min(x_train[:, 1])
x_train_max = max(x_train[:, 1])

x_1_values = np.linspace(x_train_min - 1, x_train_max + 1, 100)
decision_boundaries = []
for model in models:
    x = -((model.theta[0] + model.theta[1]
          * x_1_values) / model.theta[2])
    decision_boundaries.append(x)

plt.scatter(class_0[:, 0], class_0[:, 1], marker='o', c='red', label='class 0')
plt.scatter(class_1[:, 0], class_1[:, 1],
            marker='x', c='black', label='class 1')
for lambda_value, boundary in zip(lambda_values, decision_boundaries):
    plt.plot(x_1_values, boundary, label=f'{lambda_value}')

plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.legend()
plt.show()

plt.plot(lambda_values, training_losses, label='training')
plt.plot(lambda_values, validation_losses, label='validation')
plt.xlabel('lambda')
plt.ylabel('loss')
plt.title('Training and Validation Loss vs Regularization Strength')
plt.legend()
plt.show()

gap = []
for validation_loss, training_loss in zip(validation_losses, training_losses):
    gap.append(validation_loss - training_loss)

print(gap)
