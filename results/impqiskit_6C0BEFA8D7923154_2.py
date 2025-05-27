# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 333c , Prev_Value 3333 , Rem Cost 700

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 1e1b  BS[2] 5555  BS[3] 333c , Prev_Value 0f0f , Rem Cost 1400

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 1e1b  BS[2] 5555  BS[3] ccc3 , Prev_Value 333c , Rem Cost 1500

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 1e1b  BS[2] 5555  BS[3] ccc3 , Prev_Value 14ee , Rem Cost 2000 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 14ee  BS[1] 1e1b  BS[2] 5555  BS[3] ccc3 , Prev_Value 4b4e , Rem Cost 1300 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 14ee  BS[1] 1e1b  BS[2] 4b4e  BS[3] ccc3 , Prev_Value d2d8 , Rem Cost 1100 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 14ee  BS[1] d2d8  BS[2] 4b4e  BS[3] ccc3 , Prev_Value 5fa0 , Rem Cost 900 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 14ee  BS[1] d2d8  BS[2] 5fa0  BS[3] ccc3 , Prev_Value 9e58 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : 5FA0 CCC3 9E58 14EE 
# T-Depth : 4
# Depth : 32
