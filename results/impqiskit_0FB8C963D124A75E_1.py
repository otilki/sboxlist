# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(0))
circuit.x(3)
circuit.x(1)
circuit.cx((2),(1))
circuit.ccx((2),(0),(3))
circuit.cx((3),(2))
circuit.ccx((2),(1),(0))
#circuit.cccx((0),(2),(3),(1))
#Qiskit doesn't natively support CCCX gates.
circuit.cx((0),(3))
circuit.cx((1),(0))
circuit.x(2)
circuit.ccx((3),(2),(1))
circuit.ccx((1),(0),(2))
circuit.x(0)
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[1];
#X[3] = F[2];

# to : 7C89 4A97 632D 65C6 
# T-Depth : 7
# Depth : 59
