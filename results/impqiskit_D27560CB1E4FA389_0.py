# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
circuit.ccx((3),(0),(1))
circuit.ccx((2),(1),(0))
circuit.cx((3),(2))
circuit.cx((1),(3))
#circuit.cccx((0),(1),(3),(2))
#Qiskit doesn't natively support CCCX gates.
circuit.ccx((2),(0),(1))
circuit.cx((0),(1))
circuit.cx((2),(3))
circuit.ccx((3),(1),(2))
circuit.cx((3),(0))
circuit.cx((2),(1))
circuit.x(0)
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[0];

# to : 835B BA70 695C B195 
# T-Depth : 7
# Depth : 59
