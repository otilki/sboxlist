# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[0];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 11ee  BS[3] 3333 , Prev_Value 00ff , Rem Cost 700

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] 11ee  BS[3] 3333 , Prev_Value 5555 , Rem Cost 900

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 11ee  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 1100

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 2dd2  BS[3] 3333 , Prev_Value 11ee , Rem Cost 1300

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 2dd2  BS[3] 7788 , Prev_Value 3333 , Rem Cost 1500

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 695a  BS[3] 7788 , Prev_Value 2dd2 , Rem Cost 2200

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 695a  BS[3] 7788 , Prev_Value 70b3 , Rem Cost 1900 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 70b3  BS[2] 695a  BS[3] 7788 , Prev_Value 4bb4 , Rem Cost 1200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 70b3  BS[2] 695a  BS[3] 7788 , Prev_Value 96a5 , Rem Cost 1000 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 70b3  BS[2] 96a5  BS[3] 7788 , Prev_Value e616 , Rem Cost 900 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] e616  BS[2] 96a5  BS[3] 7788 , Prev_Value 359c , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[0];

# to : 359C E616 96A5 4BB4 
# T-Depth : 4
# Depth : 34
