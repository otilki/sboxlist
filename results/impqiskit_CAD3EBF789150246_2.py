# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[2];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 5a5a  BS[2] 3333  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 1

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 50af  BS[1] 5a5a  BS[2] 3333  BS[3] 5555 , Prev_Value 00ff , Rem Cost 101

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 50af  BS[1] 5a5a  BS[2] 639c  BS[3] 5555 , Prev_Value 3333 , Rem Cost 102

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 50af  BS[1] 5a5a  BS[2] 639c  BS[3] aaaa , Prev_Value 5555 , Rem Cost 103

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 50af  BS[1] 5a5a  BS[2] 9c63  BS[3] aaaa , Prev_Value 639c , Rem Cost 104

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 50af  BS[1] 5a5a  BS[2] 9c63  BS[3] faa0 , Prev_Value aaaa , Rem Cost 204

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 50af  BS[1] 5a5a  BS[2] 9c63  BS[3] faa0 , Prev_Value c88f , Rem Cost 204 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] c88f  BS[1] 5a5a  BS[2] 9c63  BS[3] faa0 , Prev_Value 3770 , Rem Cost 104 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3770  BS[1] 5a5a  BS[2] 9c63  BS[3] faa0 , Prev_Value a5a5 , Rem Cost 103 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3770  BS[1] a5a5  BS[2] 9c63  BS[3] faa0 , Prev_Value 5f05 , Rem Cost 102 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3770  BS[1] 5f05  BS[2] 9c63  BS[3] faa0 , Prev_Value eec0 , Rem Cost 101 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3770  BS[1] 5f05  BS[2] 9c63  BS[3] eec0 , Prev_Value ab13 , Rem Cost 1 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[0];

# to : EEC0 AB13 5F05 3770 
# T-Depth : 4
# Depth : 36
