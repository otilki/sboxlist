# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 1e1e  BS[1] 3333  BS[2] 5555  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 700

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 1e1e  BS[1] 3333  BS[2] 6666  BS[3] 00ff , Prev_Value 5555 , Rem Cost 900

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ee1  BS[1] 3333  BS[2] 6666  BS[3] 00ff , Prev_Value 1e1e , Rem Cost 1100

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1ee1  BS[1] 3333  BS[2] 6666  BS[3] 6699 , Prev_Value 00ff , Rem Cost 1300

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 1ee1  BS[1] 2dd2  BS[2] 6666  BS[3] 6699 , Prev_Value 3333 , Rem Cost 1500

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1ee1  BS[1] 4bd2  BS[2] 6666  BS[3] 6699 , Prev_Value 2dd2 , Rem Cost 2200

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 1ee1  BS[1] 4bd2  BS[2] 6666  BS[3] 6699 , Prev_Value 6c59 , Rem Cost 1900 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 1ee1  BS[1] 4bd2  BS[2] 6666  BS[3] 6c59 , Prev_Value e11e , Rem Cost 1200 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] e11e  BS[1] 4bd2  BS[2] 6666  BS[3] 6c59 , Prev_Value 8778 , Rem Cost 1100 R

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] e11e  BS[1] 4bd2  BS[2] 8778  BS[3] 6c59 , Prev_Value a94e , Rem Cost 900 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] a94e  BS[1] 4bd2  BS[2] 8778  BS[3] 6c59 , Prev_Value e29c , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[3];
#X[3] = F[1];

# to : A94E 8778 6C59 E29C 
# T-Depth : 4
# Depth : 37
