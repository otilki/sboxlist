# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[0];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
circuit.ccx((2),(1),(0))
circuit.cx((0),(2))
circuit.ccx((3),(2),(1))
circuit.cx((1),(3))
circuit.ccx((3),(0),(1))
circuit.ccx((3),(1),(0))
circuit.cx((0),(2))
circuit.cx((0),(3))
circuit.ccx((3),(2),(0))
circuit.ccx((1),(0),(3))
circuit.x(0)
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[2];

# to : F5C0 8765 4CE9 517C 
# T-Depth : 6
# Depth : 51
