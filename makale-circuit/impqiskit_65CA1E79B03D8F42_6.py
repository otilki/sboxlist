# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[1];
#F[2] = X[0];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 0f0f  BS[2] 00ff  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] 0f0f  BS[2] 00ff  BS[3] cccc , Prev_Value 3333 , Rem Cost 200

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] f0f0  BS[2] 00ff  BS[3] cccc , Prev_Value 0f0f , Rem Cost 300

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] f0f0  BS[2] 8877  BS[3] cccc , Prev_Value 00ff , Rem Cost 1000

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2ada  BS[1] f0f0  BS[2] 8877  BS[3] cccc , Prev_Value aaaa , Rem Cost 1700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 2ada  BS[1] f0f0  BS[2] 7788  BS[3] cccc , Prev_Value 8877 , Rem Cost 1800

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2ada  BS[1] 3c3c  BS[2] 7788  BS[3] cccc , Prev_Value f0f0 , Rem Cost 2000

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2ada  BS[1] 3c3c  BS[2] 7788  BS[3] cccc , Prev_Value 4bb4 , Rem Cost 1900 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2ada  BS[1] 4bb4  BS[2] 7788  BS[3] cccc , Prev_Value e616 , Rem Cost 1700 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2ada  BS[1] 4bb4  BS[2] 7788  BS[3] e616 , Prev_Value 695a , Rem Cost 1500 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 695a  BS[1] 4bb4  BS[2] 7788  BS[3] e616 , Prev_Value 359c , Rem Cost 800 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 695a  BS[1] 4bb4  BS[2] 359c  BS[3] e616 , Prev_Value 96a5 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[1];

# to : 359C E616 96A5 4BB4 
# T-Depth : 4
# Depth : 33
