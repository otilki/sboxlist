# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] 00ff , Prev_Value 5555 , Rem Cost 200

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] ff00 , Prev_Value 00ff , Rem Cost 300

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] f0f0  BS[1] 3333  BS[2] 55aa  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 400

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] f0f0  BS[1] 3333  BS[2] 55aa  BS[3] ee22 , Prev_Value ff00 , Rem Cost 1100

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] f0f0  BS[1] c3c3  BS[2] 55aa  BS[3] ee22 , Prev_Value 3333 , Rem Cost 1300

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] f0f0  BS[1] c3c3  BS[2] bb88  BS[3] ee22 , Prev_Value 55aa , Rem Cost 1500

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ed2  BS[1] c3c3  BS[2] bb88  BS[3] ee22 , Prev_Value f0f0 , Rem Cost 1700

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] bb88  BS[3] ee22 , Prev_Value c3c3 , Rem Cost 2400

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] bb88  BS[3] ee22 , Prev_Value b34a , Rem Cost 1800 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] b34a  BS[3] ee22 , Prev_Value 87e1 , Rem Cost 1100 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] b34a  BS[3] 87e1 , Prev_Value ad98 , Rem Cost 900 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] ad98  BS[1] 69c3  BS[2] b34a  BS[3] 87e1 , Prev_Value 26e9 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[2];

# to : 69C3 26E9 AD98 B34A 
# T-Depth : 4
# Depth : 37
