import numpy as np


class LinearRegression:

    def __init__(self, lr: float, max_iter: int, dim=None):
        self.lr = lr
        self.max_iter = max_iter
        self.w = np.random.rand(1, dim) if dim is not None else None
        self.b = np.random.random()
        self.X = None
        self.y = None
        self.pred = None

    def _grad(self):
        preds = self.predict(self.X)
        n = self.X.shape[0]
        dw = - (2/n * self.X.T.dot(self.y - preds).T)
        db = - (2 / n * np.sum(self.y - preds))
        return dw, db

    def _update(self):
        dw, db = self._grad()
        self.w -= self.lr * dw
        self.b -= self.lr * db

    def fit(self, X, y):
        self.X = X
        self.y = y[:, np.newaxis]
        if self.w is None:
            self.w = np.random.rand(1, X.shape[1])
        for iter in range(self.max_iter):
            self._update()

    def predict(self, X):
        return X.dot(self.w.T) + self.b
