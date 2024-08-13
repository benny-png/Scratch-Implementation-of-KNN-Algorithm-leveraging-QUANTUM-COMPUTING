from qiskit.quantum_info import Statevector

def quantum_distance(circuit1, circuit2):
    state1 = Statevector.from_instruction(circuit1)
    state2 = Statevector.from_instruction(circuit2)
    return 1 - abs(state1.inner(state2))**2