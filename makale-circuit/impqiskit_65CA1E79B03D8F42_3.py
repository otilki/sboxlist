# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 3333  BS[3] 11ee , Prev_Value 00ff , Rem Cost 700

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] 3333  BS[3] 11ee , Prev_Value 5555 , Rem Cost 900

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] 3333  BS[3] ee11 , Prev_Value 11ee , Rem Cost 1000

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 3333  BS[3] ee11 , Prev_Value 0f0f , Rem Cost 1200

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 7788  BS[3] ee11 , Prev_Value 3333 , Rem Cost 1400

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 7788  BS[3] aa99 , Prev_Value ee11 , Rem Cost 2100

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 7788  BS[3] aa99 , Prev_Value 70b3 , Rem Cost 2000 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 70b3  BS[2] 7788  BS[3] aa99 , Prev_Value 96a5 , Rem Cost 1300 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 70b3  BS[2] 7788  BS[3] 96a5 , Prev_Value e616 , Rem Cost 1100 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] e616  BS[2] 7788  BS[3] 96a5 , Prev_Value 4bb4 , Rem Cost 900 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] e616  BS[2] 7788  BS[3] 96a5 , Prev_Value 359c , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[0];

# to : 359C E616 96A5 4BB4 
# T-Depth : 4
# Depth : 36
