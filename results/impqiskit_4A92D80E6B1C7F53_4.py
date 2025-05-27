# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 5a5a  BS[2] 5555  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 200

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5a5a  BS[2] 6666  BS[3] 3333 , Prev_Value 5555 , Rem Cost 400

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5a5a  BS[2] 6666  BS[3] cccc , Prev_Value 3333 , Rem Cost 500

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] ff00  BS[1] 5a5a  BS[2] 6666  BS[3] cccc , Prev_Value 00ff , Rem Cost 600

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] ff00  BS[1] a55a  BS[2] 6666  BS[3] cccc , Prev_Value 5a5a , Rem Cost 800

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] ff00  BS[1] a55a  BS[2] c366  BS[3] cccc , Prev_Value 6666 , Rem Cost 1500

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] ff00  BS[1] 6996  BS[2] c366  BS[3] cccc , Prev_Value a55a , Rem Cost 1700

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c66  BS[1] 6996  BS[2] c366  BS[3] cccc , Prev_Value ff00 , Rem Cost 1900

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3c66  BS[1] 6996  BS[2] c366  BS[3] e4ca , Prev_Value cccc , Rem Cost 2600

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c66  BS[1] 6996  BS[2] c366  BS[3] e4ca , Prev_Value 3c99 , Rem Cost 2100 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3c66  BS[1] 6996  BS[2] 3c99  BS[3] e4ca , Prev_Value 14f6 , Rem Cost 2000 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 14f6  BS[1] 6996  BS[2] 3c99  BS[3] e4ca , Prev_Value 6d54 , Rem Cost 1300 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 14f6  BS[1] 6d54  BS[2] 3c99  BS[3] e4ca , Prev_Value 286f , Rem Cost 600 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 286f  BS[1] 6d54  BS[2] 3c99  BS[3] e4ca , Prev_Value 899e , Rem Cost 400 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 286f  BS[1] 6d54  BS[2] 3c99  BS[3] 899e , Prev_Value 51cd , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[0];

# to : 6D54 899E 51CD 286F 
# T-Depth : 4
# Depth : 38
