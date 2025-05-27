# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[0];
#F[2] = X[2];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(3))
circuit.ccx((3),(1),(0))
circuit.cx((0),(1))
circuit.cx((1),(2))
circuit.cx((2),(3))
#circuit.cccx((0),(1),(3),(2))
#Qiskit doesn't natively support CCCX gates.
circuit.ccx((2),(0),(1))
circuit.ccx((3),(1),(0))
circuit.cx((3),(1))
circuit.ccx((1),(0),(3))
circuit.cx((1),(2))
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[3];

# to : 0BD6 59E1 6378 6593 
# T-Depth : 7
# Depth : 61
