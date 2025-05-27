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

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 5a5a  BS[3] 50af , Prev_Value 00ff , Rem Cost 101

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 055f  BS[1] 3333  BS[2] 5a5a  BS[3] 50af , Prev_Value 5555 , Rem Cost 201

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 055f  BS[1] 3333  BS[2] 5a5a  BS[3] 639c , Prev_Value 50af , Rem Cost 202

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 055f  BS[1] 3333  BS[2] 5f05  BS[3] 639c , Prev_Value 5a5a , Rem Cost 203

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 055f  BS[1] 3333  BS[2] 5f05  BS[3] 639c , Prev_Value 9c63 , Rem Cost 203 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 055f  BS[1] 3333  BS[2] 5f05  BS[3] 9c63 , Prev_Value 3770 , Rem Cost 202 R

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 055f  BS[1] 3770  BS[2] 5f05  BS[3] 9c63 , Prev_Value 113f , Rem Cost 102 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 113f  BS[1] 3770  BS[2] 5f05  BS[3] 9c63 , Prev_Value eec0 , Rem Cost 2 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] eec0  BS[1] 3770  BS[2] 5f05  BS[3] 9c63 , Prev_Value ab13 , Rem Cost 1 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[1];

# to : EEC0 AB13 5F05 3770 
# T-Depth : 4
# Depth : 35
