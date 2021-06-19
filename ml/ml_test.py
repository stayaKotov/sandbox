from lin_reg import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

if __name__ == "__main__":
    lin_reg = LinearRegression(0.01, 900, 2)
    X = np.random.rand(1000, 2)
    y = X[:, 0] * 2 + X[:, 1] * 3
    preds = lin_reg.predict(X)
    mean_before = mean_squared_error(y, preds)
    lin_reg.fit(X, y)
    preds2 = lin_reg.predict(X)
    mean_after = mean_squared_error(y, preds2)
    print(f"mean_before = {mean_before}")
    print(f"mean_after = {mean_after}")

    plt.figure(figsize=(15,10))
    plt.scatter(X[:,0], y, label="true")
    plt.scatter(X[:,0], preds, label="pred1")
    plt.scatter(X[:,0], preds2, label="pred2")
    plt.legend()
    plt.show()
