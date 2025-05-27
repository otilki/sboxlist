# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] f0f0  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 100

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 3333  BS[2] f0f0  BS[3] 5555 , Prev_Value 00ff , Rem Cost 300

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 3333  BS[2] f0f0  BS[3] 4477 , Prev_Value 5555 , Rem Cost 1000

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] f0f0  BS[3] 4477 , Prev_Value 3333 , Rem Cost 1700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] f0f0  BS[3] bb88 , Prev_Value 4477 , Rem Cost 1800

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] a55a  BS[3] bb88 , Prev_Value f0f0 , Rem Cost 2000

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] a55a  BS[3] bb88 , Prev_Value 26e9 , Rem Cost 2000 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 26e9  BS[1] 7343  BS[2] a55a  BS[3] bb88 , Prev_Value 1ed2 , Rem Cost 1800 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 26e9  BS[1] 7343  BS[2] 1ed2  BS[3] bb88 , Prev_Value 69c3 , Rem Cost 1600 R

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 26e9  BS[1] 69c3  BS[2] 1ed2  BS[3] bb88 , Prev_Value b34a , Rem Cost 900 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 26e9  BS[1] 69c3  BS[2] 1ed2  BS[3] b34a , Prev_Value ad98 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[0];
#X[2] = F[2];
#X[3] = F[3];

# to : 69C3 26E9 AD98 B34A 
# T-Depth : 4
# Depth : 36
