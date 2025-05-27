# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[1];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 3c3c  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 200

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 3cc3  BS[3] 5555 , Prev_Value 3c3c , Rem Cost 400

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 3cc3  BS[3] 6996 , Prev_Value 5555 , Rem Cost 600

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 3cf0  BS[3] 6996 , Prev_Value 3cc3 , Rem Cost 1300

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0fc3  BS[1] 00ff  BS[2] 3cf0  BS[3] 6996 , Prev_Value 3333 , Rem Cost 1500

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 3cf0  BS[3] 6996 , Prev_Value 00ff , Rem Cost 2200

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 3cf0  BS[3] 6996 , Prev_Value 14f6 , Rem Cost 2100 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 14f6  BS[3] 6996 , Prev_Value 6d54 , Rem Cost 1400 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 14f6  BS[3] 6d54 , Prev_Value 79a2 , Rem Cost 700 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 79a2  BS[3] 6d54 , Prev_Value 7661 , Rem Cost 500 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 7661  BS[1] 286f  BS[2] 79a2  BS[3] 6d54 , Prev_Value 51cd , Rem Cost 300 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 7661  BS[1] 286f  BS[2] 51cd  BS[3] 6d54 , Prev_Value 899e , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[2];
#X[3] = F[1];

# to : 6D54 899E 51CD 286F 
# T-Depth : 4
# Depth : 42
