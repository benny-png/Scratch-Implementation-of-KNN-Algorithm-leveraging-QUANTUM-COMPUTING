import matplotlib.pyplot as plt
import numpy as np

def plot_results(X, y, test_point, distances, k, output_file='visualization/plot.png'):
    """
    Visualizes the data points, test point, and connections to the nearest neighbors.
    """
    X = np.array(X)  # Ensure X is a NumPy array
    nearest_neighbors = sorted(distances, key=lambda x: x[0])[:k]

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', label='Training Data')
    plt.colorbar(scatter, label='Class')

    plt.scatter(*test_point, color='red', marker='X', s=100, label='Test Point')

    for dist, label, index in nearest_neighbors:
        # Use the correct index to draw lines to the nearest neighbors
        plt.plot([test_point[0], X[index, 0]], [test_point[1], X[index, 1]], 'k--', lw=1)

    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('KNN Classification Visualization')
    plt.legend()
    plt.grid(True)
    
    plt.savefig(output_file)
    plt.show()
