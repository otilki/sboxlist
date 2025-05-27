# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(2))
circuit.cx((1),(2))
circuit.ccx((2),(1),(3))
circuit.ccx((3),(0),(1))
circuit.x(3)
circuit.ccx((1),(0),(2))
#circuit.cccx((1),(2),(3),(0))
#Qiskit doesn't natively support CCCX gates.
circuit.cx((0),(3))
circuit.ccx((3),(2),(0))
circuit.cx((1),(0))
circuit.ccx((2),(0),(1))
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[0];
#X[2] = F[1];
#X[3] = F[3];

# to : 5B86 6E52 0F65 9D32 
# T-Depth : 8
# Depth : 64
