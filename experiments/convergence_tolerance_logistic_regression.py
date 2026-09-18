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

model_1 = LogisticRegression(10000, 1.0, 1e-2)
model_2 = LogisticRegression(10000, 1.0, 1e-5)
model_3 = LogisticRegression(10000, 1.0, 1e-8)

model_1.fit(X, y)
model_2.fit(X, y)
model_3.fit(X, y)

models = [model_1, model_2, model_3]


def print_model_details(models):
    for model in models:
        theta_history = np.array(model.theta_history)
        update_diff = np.diff(theta_history, axis=0)
        update_magnitude = np.linalg.norm(update_diff, axis=(2, 1))
        print(f'Epsilon - {model.eps}')
        print(f'loss : {model.loss_history[-1]}')
        print(f'iterations : {model.n_iterations}')
        print(f'Theta : {model.theta_history[-1]}')
        print(f'Update magnitde : {update_magnitude[-1]}')


def plot_loss_vs_iteration(models):
    plt.figure()
    for model in models:
        x_iterations = np.arange(0, len(model.loss_history))
        plt.plot(x_iterations, model.loss_history,
                 label=f'epsilon - {model.eps}')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.title('Loss vs Iterations')
    plt.legend()
    plt.show()


plot_loss_vs_iteration(models)
