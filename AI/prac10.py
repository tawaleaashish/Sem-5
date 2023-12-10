import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, learning_rate=0.02, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.errors = []

        for _ in range(self.n_iterations):
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, 0)

# Generate linearly separable data points
np.random.seed(0)
class1_x = np.random.normal(2, 1, 50)
class1_y = np.random.normal(2, 1, 50)
class2_x = np.random.normal(6, 1, 50)
class2_y = np.random.normal(6, 1, 50)

# Create dataset and labels
data_x = np.concatenate((class1_x, class2_x))
data_y = np.concatenate((class1_y, class2_y))
labels = np.concatenate((np.zeros(50), np.ones(50)))

# Create and train the custom Perceptron model
perceptron = Perceptron(learning_rate=0.1, n_iterations=1000)
perceptron.fit(np.column_stack((data_x, data_y)), labels)

# Plot the decision boundary
x = np.linspace(min(data_x), max(data_x), 100)
y = (-perceptron.weights[1] / perceptron.weights[2]) * x - perceptron.weights[0] / perceptron.weights[2]

plt.scatter(data_x, data_y, c=labels, cmap='viridis')
plt.plot(x, y, '-r', label='Decision Boundary')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Perceptron Decision Boundary')
plt.legend()
plt.show()
print(f"Weights: {perceptron.weights[1]},{perceptron.weights[2]} | Bias: {perceptron.weights[0]}")