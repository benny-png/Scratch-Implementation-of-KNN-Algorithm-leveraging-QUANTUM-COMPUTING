import numpy as np
from quantum_processes.encoding import encode_data
from classical_processes.knn_logic import classify
from visualization.plot_results_classical import plot_results
from scipy.spatial.distance import euclidean

# Example data points
X = [
    [1, 2], [2, 3], [3, 1], [5, 4],
    [6, 2], [7, 5], [8, 3], [4, 5],
    [2, 7], [3, 6], [5, 8], [6, 6]
]
y = [
    0, 0, 1, 1,
    0, 1, 1, 0,
    0, 1, 1, 0
]

# Define test points
test_points = [[4, 3], [6, 4]]

for test_point in test_points:
    # Calculate distances using Euclidean distance without scaling
    distances = []
    for i in range(len(X)):
        distance = euclidean(test_point, X[i])
        distances.append((distance, y[i], i))

    # Sort distances in ascending order to get the smallest distances
    distances.sort()
    k = 3
    nearest_neighbors = distances[:k]
    prediction = classify(nearest_neighbors, k)
    print(f"Predicted class for test point {test_point}: {prediction}")

    # Plot results
    plot_results(X, y, test_point, nearest_neighbors, k)
