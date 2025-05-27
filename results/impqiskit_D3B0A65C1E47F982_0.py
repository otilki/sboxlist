# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 200

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 8787  BS[3] cccc , Prev_Value 0f0f , Rem Cost 900

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aa55  BS[2] 8787  BS[3] cccc , Prev_Value aaaa , Rem Cost 1100

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6699  BS[2] 8787  BS[3] cccc , Prev_Value aa55 , Rem Cost 1300

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 6699  BS[2] 8787  BS[3] cc55 , Prev_Value cccc , Rem Cost 2000

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6699  BS[2] 8787  BS[3] cc55 , Prev_Value e29c , Rem Cost 2000 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] e29c  BS[2] 8787  BS[3] cc55 , Prev_Value 8778 , Rem Cost 1300 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 8778  BS[1] e29c  BS[2] 8787  BS[3] cc55 , Prev_Value 651b , Rem Cost 1100 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 8778  BS[1] e29c  BS[2] 651b  BS[3] cc55 , Prev_Value a94e , Rem Cost 900 R

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 8778  BS[1] e29c  BS[2] a94e  BS[3] cc55 , Prev_Value 6c59 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[0];
#X[2] = F[3];
#X[3] = F[1];

# to : A94E 8778 6C59 E29C 
# T-Depth : 4
# Depth : 39
