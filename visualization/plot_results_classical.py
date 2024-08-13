import matplotlib.pyplot as plt
import numpy as np

def plot_results(X, y, test_point, distances, k, output_file='visualization/plot.png'):
    """
    Visualizes the data points, test point, and connections to the nearest neighbors.
    """
    X = np.array(X)  # Ensure X is a NumPy array
    
    # Sort distances and extract indices of the nearest neighbors
    nearest_neighbors = sorted(distances, key=lambda x: x[0])[:k]
    neighbor_indices = [dist[2] for dist in nearest_neighbors]

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', label='Training Data')
    plt.colorbar(scatter, label='Class')

    plt.scatter(*test_point, color='red', marker='X', s=100, label='Test Point')

    for index in neighbor_indices:
        plt.plot([test_point[0], X[index, 0]], [test_point[1], X[index, 1]], 'k--', lw=1)

    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('KNN Classification Visualization')
    plt.legend()
    plt.grid(True)
    
    plt.savefig(output_file)
    plt.show()
