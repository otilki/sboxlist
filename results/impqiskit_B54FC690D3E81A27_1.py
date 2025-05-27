# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[1];
#F[2] = X[0];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(1))
circuit.ccx((3),(1),(0))
circuit.cx((0),(3))
circuit.cx((1),(2))
circuit.cx((0),(1))
#circuit.cccx((0),(2),(3),(1))
#Qiskit doesn't natively support CCCX gates.
circuit.ccx((3),(1),(2))
circuit.ccx((2),(1),(0))
circuit.cx((2),(3))
circuit.x(0)
circuit.ccx((3),(0),(1))
circuit.x(1)
circuit.cx((1),(2))
print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : 9AB4 7CA1 9467 D2C9 
# T-Depth : 7
# Depth : 60
