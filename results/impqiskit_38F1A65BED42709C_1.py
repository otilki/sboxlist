# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 55aa  BS[2] 3333  BS[3] 00ff , Prev_Value 5555 , Rem Cost 200

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 55aa  BS[2] 3333  BS[3] 11dd , Prev_Value 00ff , Rem Cost 900

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ed2  BS[1] 55aa  BS[2] 3333  BS[3] 11dd , Prev_Value 0f0f , Rem Cost 1100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 1ed2  BS[1] 55aa  BS[2] 3333  BS[3] ee22 , Prev_Value 11dd , Rem Cost 1200

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 1ed2  BS[1] 55aa  BS[2] 2de1  BS[3] ee22 , Prev_Value 3333 , Rem Cost 1400

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1ed2  BS[1] 55aa  BS[2] 69c3  BS[3] ee22 , Prev_Value 2de1 , Rem Cost 2100

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1ed2  BS[1] 55aa  BS[2] 69c3  BS[3] ee22 , Prev_Value 5d68 , Rem Cost 2000 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 1ed2  BS[1] 5d68  BS[2] 69c3  BS[3] ee22 , Prev_Value b34a , Rem Cost 1300 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1ed2  BS[1] b34a  BS[2] 69c3  BS[3] ee22 , Prev_Value 87e1 , Rem Cost 1100 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ed2  BS[1] b34a  BS[2] 69c3  BS[3] 87e1 , Prev_Value ad98 , Rem Cost 900 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] ad98  BS[1] b34a  BS[2] 69c3  BS[3] 87e1 , Prev_Value 26e9 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[1];

# to : 69C3 26E9 AD98 B34A 
# T-Depth : 4
# Depth : 38
