# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[1];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 0f0f  BS[2] 3333  BS[3] 00ff , Prev_Value 5555 , Rem Cost 100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] 0f0f  BS[2] 3333  BS[3] ff00 , Prev_Value 00ff , Rem Cost 200

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] f0f0  BS[2] 3333  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 300

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] f0f0  BS[2] 9999  BS[3] ff00 , Prev_Value 3333 , Rem Cost 500

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] 7878  BS[2] 9999  BS[3] ff00 , Prev_Value f0f0 , Rem Cost 1200

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 33aa  BS[1] 7878  BS[2] 9999  BS[3] ff00 , Prev_Value aaaa , Rem Cost 1900

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 33aa  BS[1] 7878  BS[2] 9999  BS[3] ff00 , Prev_Value a9b1 , Rem Cost 2400 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 33aa  BS[1] 7878  BS[2] a9b1  BS[3] ff00 , Prev_Value 56b1 , Rem Cost 1700 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 33aa  BS[1] 7878  BS[2] 56b1  BS[3] ff00 , Prev_Value 4bd2 , Rem Cost 1500 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 4bd2  BS[1] 7878  BS[2] 56b1  BS[3] ff00 , Prev_Value 8778 , Rem Cost 1300 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 4bd2  BS[1] 7878  BS[2] 56b1  BS[3] 8778 , Prev_Value 1d63 , Rem Cost 1100 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1d63  BS[1] 7878  BS[2] 56b1  BS[3] 8778 , Prev_Value 6c59 , Rem Cost 900 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1d63  BS[1] 6c59  BS[2] 56b1  BS[3] 8778 , Prev_Value a94e , Rem Cost 200 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 1d63  BS[1] 6c59  BS[2] a94e  BS[3] 8778 , Prev_Value e29c , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : A94E 8778 6C59 E29C 
# T-Depth : 4
# Depth : 36
