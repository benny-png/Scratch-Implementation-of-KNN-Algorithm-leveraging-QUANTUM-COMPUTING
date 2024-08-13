# STILL IN DEVELOPMENT

from quantum_processes.encoding import encode_data
from quantum_processes.distance import quantum_distance
from classical_processes.data_preprocessing import scale_data
from classical_processes.knn_logic import classify
from visualization.plot_results import plot_results

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

# Scale data
X_scaled = scale_data(X)

# Define and encode test points
test_points = [[4, 3], [6, 4]]
test_points_scaled = scale_data(test_points)
test_states = [encode_data(point) for point in test_points_scaled]

for test_point, test_state in zip(test_points, test_states):
    # Calculate distances for each test point
    distances = []
    for i in range(len(X_scaled)):
        train_state = encode_data(X_scaled[i])
        distance = quantum_distance(test_state, train_state)
        distances.append((distance, y[i], i))  # Include index i in the tuple

    # Sort distances in ascending order to get the smallest distances
    distances.sort()
    k = 3
    nearest_neighbors = distances[:k]
    prediction = classify(nearest_neighbors, k)
    print(f"Predicted class for test point {test_point}: {prediction}")

    # Plot results
    plot_results(X, y, test_point, nearest_neighbors, k)
