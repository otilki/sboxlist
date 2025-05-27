# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[2];
#F[2] = X[0];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(2))
circuit.x(3)
circuit.cx((3),(0))
circuit.ccx((2),(1),(3))
circuit.cx((0),(1))
circuit.cx((3),(0))
circuit.cx((2),(0))
circuit.ccx((3),(1),(2))
circuit.ccx((2),(0),(1))
circuit.cx((1),(2))
circuit.ccx((3),(2),(0))
circuit.ccx((1),(0),(3))
circuit.cx((3),(0))
circuit.x(0)
circuit.x(2)
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[0];
#X[2] = F[3];
#X[3] = F[2];

# to : 8F86 4C6E F8C4 ED09 
# T-Depth : 5
# Depth : 51
