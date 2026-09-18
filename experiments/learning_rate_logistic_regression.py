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


def plot_sigmoid_curve(X, y, models):
    x = X[:, -1]
    x_plot = np.linspace(x.min(), x.max(), 100)
    y_plot = y.flatten()

    plt.figure()
    for model in models:
        z = model.theta[0] + model.theta[1] * x_plot
        h_plot = model.sigmoid(z)
        x_boundary = -(model.theta[0]/model.theta[1])
        plt.vlines(x_boundary, 0, 1,
                   label=f"Decision Boundary (x = {x_boundary.item():.2f}), learning rate = {model.learning_rate}")

        plt.plot(x_plot, h_plot, label=f'{model.learning_rate}')
    plt.xlabel('Feature 1')
    plt.ylabel('Probability of class 1')
    plt.title('Logistic Regression h(x) vs x_1')

    x_0 = x[y_plot == 0]
    x_1 = x[y_plot == 1]

    plt.scatter(x_0, np.zeros_like(x_0), label='class 0')
    plt.scatter(x_1, np.ones_like(x_1), label='class 1')

    plt.axhline(0.5)
    plt.legend()
    plt.show()

# LOSS vs iteration


def plot_loss_vs_iteration(models):
    plt.figure()
    for model in models:
        x_iterations = np.arange(0, len(model.loss_history))
        plt.plot(x_iterations, model.loss_history,
                 label=f'{model.learning_rate}')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.title('Loss vs iterations')
    plt.legend()
    plt.show()

# theta vs iterations


def plot_theta_vs_iterations(model):
    theta_history = np.array(model.theta_history)
    theta_0 = theta_history[:, 0]
    theta_1 = theta_history[:, 1]
    x_iteration = np.arange(0, len(model.theta_history))

    plt.plot(x_iteration, theta_0, label='theta 0')
    plt.plot(x_iteration, theta_1, label='theta 1')
    plt.xlabel('Iterations')
    plt.ylabel('theta')
    plt.title('theta vs iterations')
    plt.legend()
    plt.show()


def plot_update_magnitude(models):
    plt.figure()
    for model in models:
        theta_history = np.array(model.theta_history)
        update_diff = np.diff(theta_history, axis=0)
        update_magnitude = np.linalg.norm(update_diff, axis=(2, 1))
        x_value = np.arange(0, len(model.theta_history) - 1)

        plt.plot(x_value, update_magnitude,
                 label=f'learning rate = {model.learning_rate}')
    plt.xlabel('Iterations')
    plt.ylabel('update magnitude')
    plt.title('update magnitude vs iterations')
    plt.legend()
    plt.show()


def print_model_details(models):
    for model in models:
        theta_history = np.array(model.theta_history)
        update_diff = np.diff(theta_history, axis=0)
        update_magnitude = np.linalg.norm(update_diff, axis=(2, 1))

        print(
            f'FINAL LOSS for {model.learning_rate} - {model.loss_history[-1]}')
        print(f'ITERATION for {model.learning_rate} - {model.n_iterations}')
        print(f'FINAL THETA for {model.learning_rate} - {model.theta}')
        print(
            f'UPDATE MAGNITUDE for {model.learning_rate} - {update_magnitude[-1]}')


lr_1 = LogisticRegression(10000, 0.01, 1e-5)
lr_2 = LogisticRegression(10000, 1.0, 1e-5)
lr_3 = LogisticRegression(10000, 10.0, 1e-5)

lr_1.fit(X, y)
lr_2.fit(X, y)
lr_3.fit(X, y)

models = [lr_1, lr_2, lr_3]

plot_sigmoid_curve(X, y, models)
plot_loss_vs_iteration(models)
plot_update_magnitude(models)

plot_theta_vs_iterations(lr_1)
plot_theta_vs_iterations(lr_2)
plot_theta_vs_iterations(lr_3)

print_model_details(models)
