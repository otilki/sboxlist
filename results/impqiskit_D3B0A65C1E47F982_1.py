# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 0f0f  BS[3] 6666 , Prev_Value 3333 , Rem Cost 200

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 0ff0  BS[3] 6666 , Prev_Value 0f0f , Rem Cost 400

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 4bb4  BS[3] 6666 , Prev_Value 0ff0 , Rem Cost 1100

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 1ee1  BS[2] 4bb4  BS[3] 6666 , Prev_Value 5555 , Rem Cost 1300

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value 4bb4 , Rem Cost 2000

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value 0a3f , Rem Cost 2100 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0a3f  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value 6c59 , Rem Cost 1400 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 6c59  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value e11e , Rem Cost 1200 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 6c59  BS[1] e11e  BS[2] 4bd2  BS[3] 6666 , Prev_Value 8778 , Rem Cost 1100 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 6c59  BS[1] e11e  BS[2] 4bd2  BS[3] 8778 , Prev_Value a94e , Rem Cost 900 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6c59  BS[1] a94e  BS[2] 4bd2  BS[3] 8778 , Prev_Value e29c , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[2];

# to : A94E 8778 6C59 E29C 
# T-Depth : 4
# Depth : 38
