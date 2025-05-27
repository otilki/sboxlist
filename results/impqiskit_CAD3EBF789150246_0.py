# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 5a5a  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 1

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] a5a5  BS[3] 00ff , Prev_Value 5a5a , Rem Cost 2

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 55f0  BS[1] 3333  BS[2] a5a5  BS[3] 00ff , Prev_Value 5555 , Rem Cost 102

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 55f0  BS[1] 66c3  BS[2] a5a5  BS[3] 00ff , Prev_Value 3333 , Rem Cost 103

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 55f0  BS[1] 66c3  BS[2] a5a5  BS[3] ff00 , Prev_Value 00ff , Rem Cost 104

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 55f0  BS[1] 66c3  BS[2] a5a5  BS[3] faa0 , Prev_Value ff00 , Rem Cost 204

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 55f0  BS[1] 66c3  BS[2] a5a5  BS[3] faa0 , Prev_Value 3770 , Rem Cost 203 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3770  BS[1] 66c3  BS[2] a5a5  BS[3] faa0 , Prev_Value 5f05 , Rem Cost 103 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3770  BS[1] 66c3  BS[2] 5f05  BS[3] faa0 , Prev_Value cdd0 , Rem Cost 102 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3770  BS[1] 66c3  BS[2] 5f05  BS[3] cdd0 , Prev_Value ab13 , Rem Cost 101 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3770  BS[1] ab13  BS[2] 5f05  BS[3] cdd0 , Prev_Value eec0 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[0];

# to : EEC0 AB13 5F05 3770 
# T-Depth : 4
# Depth : 39
