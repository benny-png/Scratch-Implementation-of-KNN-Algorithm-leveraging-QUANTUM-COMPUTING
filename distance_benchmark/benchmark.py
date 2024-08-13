import numpy as np
from scipy.spatial.distance import euclidean
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import time

# Example Classical Data Points
classical_points = [
    [1, 2], [2, 3], [3, 1], [5, 4],
    [6, 2], [7, 5], [8, 3], [4, 5]
]

# Generate Quantum Circuits corresponding to the classical points
def create_quantum_circuit(point):
    qc = QuantumCircuit(len(point))
    for i, coord in enumerate(point):
        qc.ry(coord, i)
    return qc

quantum_circuits = [create_quantum_circuit(point) for point in classical_points]

# Define quantum distance function
def quantum_distance(circuit1, circuit2):
    state1 = Statevector.from_instruction(circuit1)
    state2 = Statevector.from_instruction(circuit2)
    fidelity = abs(state1.inner(state2))**2
    return  fidelity

# Benchmark function
def benchmark_distances(classical_points, quantum_circuits):
    n = len(classical_points)
    
    classical_distances = np.zeros((n, n))
    quantum_distances = np.zeros((n, n))
    
    # Classical distance calculation
    start_time_classical = time.time()
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean(classical_points[i], classical_points[j])
            classical_distances[i, j] = classical_distances[j, i] = dist
    time_classical = time.time() - start_time_classical
    
    # Quantum distance calculation
    start_time_quantum = time.time()
    for i in range(n):
        for j in range(i+1, n):
            dist = quantum_distance(quantum_circuits[i], quantum_circuits[j])
            quantum_distances[i, j] = quantum_distances[j, i] = dist
    time_quantum = time.time() - start_time_quantum
    
    return classical_distances, quantum_distances, time_classical, time_quantum

# Run the benchmark
classical_distances, quantum_distances, time_classical, time_quantum = benchmark_distances(classical_points, quantum_circuits)

# Output results
print("Classical Distances:")
print(classical_distances)
print(f"Classical computation time: {time_classical:.6f} seconds")

print("\nQuantum Distances:")
print(quantum_distances)
print(f"Quantum computation time: {time_quantum:.6f} seconds")

# Compare results
difference = np.abs(classical_distances - quantum_distances)
print("\nDifference between classical and quantum distances:")
print(difference)
