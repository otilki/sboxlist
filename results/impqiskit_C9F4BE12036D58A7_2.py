# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] f0f0  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 100

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] f0f0  BS[3] 00ff , Prev_Value 5555 , Rem Cost 300

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] c3c3  BS[3] 00ff , Prev_Value f0f0 , Rem Cost 500

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] c3c3  BS[3] 00ff , Prev_Value 3333 , Rem Cost 1200

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] d263  BS[3] 00ff , Prev_Value c3c3 , Rem Cost 1900

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] d263  BS[3] d29c , Prev_Value 00ff , Rem Cost 2100

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] d263  BS[3] d29c , Prev_Value 665a , Rem Cost 2000 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 33f0  BS[1] 665a  BS[2] d263  BS[3] d29c , Prev_Value b439 , Rem Cost 1800 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 33f0  BS[1] 665a  BS[2] b439  BS[3] d29c , Prev_Value 2d63 , Rem Cost 1600 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 33f0  BS[1] 665a  BS[2] b439  BS[3] 2d63 , Prev_Value cc0f , Rem Cost 1500 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] cc0f  BS[1] 665a  BS[2] b439  BS[3] 2d63 , Prev_Value 6a59 , Rem Cost 1400 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] cc0f  BS[1] 6a59  BS[2] b439  BS[3] 2d63 , Prev_Value ec16 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[3];
#X[3] = F[1];

# to : EC16 B439 2D63 6A59 
# T-Depth : 4
# Depth : 35
