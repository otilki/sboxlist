# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
circuit.cx((1),(0))
circuit.cx((2),(1))
circuit.cx((3),(2))
circuit.ccx((2),(1),(0))
circuit.cx((3),(1))
circuit.cx((0),(2))
#circuit.cccx((0),(1),(2),(3))
#Qiskit doesn't natively support CCCX gates.
circuit.ccx((3),(1),(0))
circuit.ccx((3),(2),(1))
circuit.cx((1),(3))
circuit.ccx((2),(0),(1))
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[2];

# to : 9738 C92E B466 D24B 
# T-Depth : 7
# Depth : 59
