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

lr = LogisticRegression(10000, 1.0, 1e-5, theta_0=None, lambda_reg=0)
theta = lr.fit(X, y)

y_prob = lr.predict_proba(X)
y_pred = lr.predict(X)
print("\n========== Logistic Regression Test ==========")

print(f"\nFinal Theta : {theta.flatten()} \n")
print(f"\nNumber of Iterations : {lr.n_iterations}\n")

print("\nHistory Lengths")
print(f"Theta History : {len(lr.theta_history)}")
print(f"Loss History : {len(lr.loss_history)}")
print(f"Log-Likelihood : {len(lr.log_likelihood_history)}")

print("\nLoss : ")
print(f"Initial Loss : {lr.loss_history[0]:.6f}")
print(f"Final Loss : {lr.loss_history[-1]:.6f}")

print("\nLog-Likelihood: ")
print(f"Initial Log-Likelihood : {lr.log_likelihood_history[0]:.6f}")
print(f"Final Log-Likelihood : {lr.log_likelihood_history[-1]:.6f}")

print("\nPrediction : ")
print(f"probabilities of y : {y_prob.flatten()}")
print(f"predictions : {y_pred.flatten()}")

print("\nFINAL : ")
print(
    f"Final parameter change : {np.linalg.norm(lr.theta_history[-1] - lr.theta_history[-2])}")
print(f"Epsilon : {lr.eps}")

i = 1
flag = False
while i < len(lr.loss_history) and lr.loss_history[i] < lr.loss_history[i - 1]:
    i += 1
    if i == len(lr.loss_history):
        flag = True

print(f"Monotonically Decreasing Loss : {flag}")


# visualisation
# x = X[:, -1]
# y_plot = y.flatten()
# x_plot = np.linspace(x.min(), x.max(), 100)
# # print(x)
# # print(x_plot)

# z = theta[0] + theta[1] * x_plot
# h_plot = lr.sigmoid(z)

# plt.plot(x_plot, h_plot, label="sigmoid")
# plt.xlabel('Feature 1')
# plt.ylabel("probability of class 1")
# plt.title("Logistic Regression : h(x) vs x")
# # plt.show()

# x_0 = x[y_plot == 0]
# x_1 = x[y_plot == 1]

# plt.scatter(x_0, np.zeros_like(x_0), label='class 0')
# plt.scatter(x_1, np.ones_like(x_1), label='class 1')

# plt.axhline(0.5)
# x_boundary = -(theta[0] / theta[1])
# plt.vlines(x_boundary, 0, 1,
#            label=f"Decision Boundary (x = {x_boundary.item():.2f})")

# plt.legend()
# # plt.show()

# Loss vs Iteration

# x = np.arange(0, len(lr.loss_history))
# plt.plot(x, lr.loss_history)
# plt.xlabel('iteration')
# plt.ylabel('Loss')
# plt.title('Loss vs Iteration')
# plt.show()

# print(np.array(lr.theta_history).shape)

# theta_history = np.array(lr.theta_history)

# x = np.arange(0, len(lr.theta_history))
# theta_0 = theta_history[:, 0]
# theta_1 = theta_history[:, 1]

# plt.plot(x, theta_0, label="theta_0")
# plt.plot(x, theta_1, label="theta_1")
# plt.xlabel("iterations")
# plt.ylabel("Theta")
# plt.title("Theta vs Iterations")
# plt.legend()
# plt.show()

# x = np.arange(0, len(lr.theta_history) - 1)
# update_diff = np.diff(lr.theta_history, axis=0)
# update_magnitude = np.linalg.norm(update_diff, axis=(2, 1))

# plt.plot(x, update_magnitude)
# plt.xlabel("iterations")
# plt.ylabel("update magnitude")
# plt.title("Update Magnitude vs Iterations")
# plt.show()
