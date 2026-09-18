from algorithms.supervised.logistic_regression import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1, 0],
    [1, 1],
    [1, 2],
    [1, 3],
])

y = np.array([
    [0],
    [1],
    [0],
    [1]
])

model_1 = LogisticRegression(10000, 0.1, 1e-5, theta_0=None, lambda_reg=0)
model_2 = LogisticRegression(10000, 0.1, 1e-5, theta_0=None, lambda_reg=0.01)
model_3 = LogisticRegression(10000, 0.1, 1e-5, theta_0=None, lambda_reg=0.1)
model_4 = LogisticRegression(10000, 0.1, 1e-5, theta_0=None, lambda_reg=1.0)

model_1.fit(X, y)
model_2.fit(X, y)
model_3.fit(X, y)
model_4.fit(X, y)

models = [model_1, model_2, model_3, model_4]


# def print_model_details(models):
#     for model in models:
#         theta_history = np.array(model.theta_history)
#         update_diff = np.diff(theta_history, axis=0)
#         update_magnitude = np.linalg.norm(update_diff, axis=(2, 1))
#         print(f'loss : {model.loss_history[-1]}')
#         print(f'iterations : {model.n_iterations}')
#         print(f'Theta : {model.theta_history[-1]}')
#         print(f'Update magnitde : {update_magnitude[-1]}')
#         print(f'lambda : {model.lambda_reg}')
# print_model_details(models)

def print_loss(models):
    loss = []
    data_losses = []
    loss_reg = []
    for model in models:
        m = X.shape[0]
        z = np.dot(X, model.theta)
        numeric_eps = 1e-15
        h = model.sigmoid(z)
        h_safe = np.clip(h, numeric_eps, 1 - numeric_eps)
        loss_data = -(np.sum(y * np.log(h_safe) +
                      (1 - y) * np.log(1 - h_safe)) / m)
        reg_loss = model.lambda_reg*(np.sum(model.theta[1:] ** 2))
        total_loss = loss_data + reg_loss
        loss.append(total_loss)
        data_losses.append(loss_data)
        loss_reg.append(reg_loss)
    return loss, data_losses, loss_reg


loss, data_losses, loss_reg = print_loss(models)
for model, value in zip(models, loss):
    print(f'Lambda : {model.lambda_reg}, Loss : {value:.6f}')

print('\n')

for model, value in zip(models, data_losses):
    print(f'Lambda : {model.lambda_reg}, Data Loss : {value:.6f}')

print('\n')

for model, value in zip(models, loss_reg):
    print(f'Lambda : {model.lambda_reg}, Reg Loss : {value:.6f}')
