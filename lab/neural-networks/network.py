import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
    def __init__(self, learning_rate):
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bias = np.random.randn()
        self.learning_rate = learning_rate

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_deriv(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def predict(self, input_vector):
        layer1 = np.dot(input_vector, self.weights) + self.bias
        layer2 = self._sigmoid(layer1)
        return layer2

    def _compute_gradients(self, input_vector, target):
        layer1 = np.dot(input_vector, self.weights) + self.bias
        prediction = self._sigmoid(layer1)

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = self._sigmoid_deriv(layer1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

        derror_dbias = derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        derror_dweights = derror_dprediction * dprediction_dlayer1 * dlayer1_dweights

        return derror_dbias, derror_dweights

    def _update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (derror_dweights * self.learning_rate)

    def train(self, input_vectors, targets, iterations):
        cumulative_errors = []
        for current_iteration in range(iterations):
            # Pick a random data instance
            random_data_index = np.random.randint(len(input_vectors))
            input_vector = input_vectors[random_data_index]
            target = targets[random_data_index]

            # Compute the gradients and update the weights
            derror_dbias, derror_dweights = self._compute_gradients(input_vector, target)

            self._update_parameters(derror_dbias, derror_dweights)

            # Measure the cumulative error for all instances
            if current_iteration % 100 == 0:
                cumulative_error = 0
                # Measure error across all instances
                for data_instance_index in range(len(input_vectors)):
                    data_point = input_vectors[data_instance_index]
                    target = targets[data_instance_index]

                    prediction = self.predict(data_point)
                    cumulative_error += np.square(prediction - target)
                cumulative_errors.append(cumulative_error)

        return cumulative_errors

input_vectors = np.array([
    [3, 1.5], [2, 1], [4, 1.5], [3, 4],
    [3.5, 0.5], [2, 0.5], [5.5, 1], [1, 1]
])

targets = np.array([0, 1, 0, 1, 0, 1, 1, 0])

learning_rate = 0.1
iterations = 10000

nn = NeuralNetwork(learning_rate)

training_error = nn.train(input_vectors, targets, iterations)

plt.plot(training_error)
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
plt.savefig("cumulative_error.png")
