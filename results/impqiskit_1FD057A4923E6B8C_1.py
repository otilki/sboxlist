# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(3))
circuit.ccx((3),(1),(0))
circuit.cx((0),(1))
circuit.cx((1),(2))
circuit.cx((0),(3))
circuit.ccx((2),(1),(3))
#circuit.cccx((0),(2),(3),(1))
#Qiskit doesn't natively support CCCX gates.
circuit.cx((3),(1))
circuit.ccx((2),(1),(0))
circuit.cx((1),(2))
circuit.x(0)
circuit.ccx((3),(0),(1))
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[0];

# to : 6297 6D19 467C ECA4 
# T-Depth : 7
# Depth : 59
