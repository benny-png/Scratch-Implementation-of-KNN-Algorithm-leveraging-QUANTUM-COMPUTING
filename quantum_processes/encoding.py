from qiskit import QuantumCircuit
import numpy as np

def encode_data(x):
    circuit = QuantumCircuit(2)
    norm = np.linalg.norm(x)
    theta = 2 * np.arccos(x[0] / norm)
    phi = np.arctan2(x[1], x[0])
    circuit.ry(theta, 0)
    circuit.rz(phi, 0)
    return circuit
