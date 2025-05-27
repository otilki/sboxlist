# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
circuit.ccx((2),(0),(1))
circuit.ccx((3),(1),(0))
circuit.x(3)
circuit.cx((1),(2))
#circuit.cccx((0),(1),(2),(3))
#Qiskit doesn't natively support CCCX gates.
circuit.cx((2),(3))
circuit.cx((0),(2))
circuit.cx((3),(0))
circuit.ccx((2),(0),(1))
circuit.ccx((3),(1),(0))
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[0];

# to : 63C6 6D91 C6A5 5927 
# T-Depth : 7
# Depth : 58
