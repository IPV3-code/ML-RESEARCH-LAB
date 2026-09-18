import numpy as np


class LogisticRegression:
    def __init__(self, max_iter, learning_rate, eps, theta_0=None, lambda_reg=0):
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.eps = eps
        self.theta_0 = theta_0
        self.lambda_reg = lambda_reg

        self.theta = None
        self.loss_history = []
        self.log_likelihood_history = []
        self.theta_history = []

        self.n_iterations = 0

    def sigmoid(self, z):

        h = np.where(z < 0, np.exp(z) / (1 + np.exp(z)), 1 / (1 + np.exp(-z)))

        return h

    def compute_loss(self, h, y, theta, include_regularization=True):
        m = y.shape[0]
        numeric_eps = 1e-15
        h_safe = np.clip(h, numeric_eps, 1 - numeric_eps)

        if include_regularization:
            loss = -(np.sum(y * np.log(h_safe) + (1 - y) * np.log(1 -
                     h_safe)) / m) + self.lambda_reg*(np.sum(theta[1:] ** 2))
        else:
            loss = -(np.sum(y * np.log(h_safe) +
                     (1 - y) * np.log(1 - h_safe)) / m)

        return loss

    def compute_gradient(self, X, h, y, theta):
        m = X.shape[0]
        gradient_reg = np.zeros(theta.shape)
        gradient_reg[1:] = (2 * self.lambda_reg * theta[1:])
        gradient_total = (np.dot(X.T, (h - y)) / m) + gradient_reg
        return gradient_total

    def compute_log_likelihood(self, h, y):
        numerical_eps = 1e-15
        h_safe = np.clip(h, numerical_eps, 1 - numerical_eps)
        log_likelihood = (np.sum(y * np.log(h_safe) +
                          (1 - y) * np.log(1 - h_safe)))

        return log_likelihood

    def fit(self, X, y):
        n = X.shape[1]

        if self.theta_0 is None:
            self.theta_0 = np.zeros((n, 1))
        else:
            if self.theta_0.shape == (n, ):
                self.theta_0 = self.theta_0.reshape(n, 1)
            elif self.theta_0.shape != (n, 1):
                raise ValueError(
                    f'Invalid Shape for theta ! Expected shape : {(n, 1)}, But got Shape : {(self.theta_0.shape)}')

        self.theta = self.theta_0.copy()

        self.loss_history = []
        self.log_likelihood_history = []
        self.theta_history = []

        self.theta_history.append(self.theta.copy())
        self.n_iterations = 0

        while True:
            z = np.dot(X, self.theta)
            h = self.sigmoid(z)
            loss = self.compute_loss(h, y, self.theta)
            self.loss_history.append(loss)
            log_likelihood = self.compute_log_likelihood(h, y)
            self.log_likelihood_history.append(log_likelihood)

            old_theta = self.theta.copy()
            self.theta = self.theta - \
                (self.learning_rate * (self.compute_gradient(X, h, y, self.theta)))
            self.theta_history.append(self.theta.copy())

            self.n_iterations += 1

            if np.linalg.norm(old_theta - self.theta) < self.eps:
                break

            if self.n_iterations >= self.max_iter:
                break

        z = np.dot(X, self.theta)
        h = self.sigmoid(z)
        loss = self.compute_loss(h, y, self.theta)
        self.loss_history.append(loss)
        log_likelihood = self.compute_log_likelihood(h, y)
        self.log_likelihood_history.append(log_likelihood)

        return self.theta

    def predict_proba(self, X):
        z = np.dot(X, self.theta)
        h = self.sigmoid(z)

        return h

    def predict(self, X):
        h = self.predict_proba(X)
        y_pred = np.where(h >= 0.5, 1, 0)
        return y_pred
