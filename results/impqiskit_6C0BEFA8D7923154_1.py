# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 5555  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 100

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 50af  BS[2] 5555  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 800

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 50af  BS[2] 5555  BS[3] a05f , Prev_Value f0f0 , Rem Cost 1000

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 333c  BS[1] 50af  BS[2] 5555  BS[3] a05f , Prev_Value 3333 , Rem Cost 1700

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 333c  BS[1] 50af  BS[2] 5555  BS[3] a05f , Prev_Value 7549 , Rem Cost 1900 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 50af  BS[2] 7549  BS[3] a05f , Prev_Value 61a7 , Rem Cost 1200 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 333c  BS[1] 61a7  BS[2] 7549  BS[3] a05f , Prev_Value 14ee , Rem Cost 500 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 333c  BS[1] 61a7  BS[2] 14ee  BS[3] a05f , Prev_Value 5fa0 , Rem Cost 300 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 61a7  BS[2] 14ee  BS[3] 5fa0 , Prev_Value 9e58 , Rem Cost 200 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 333c  BS[1] 9e58  BS[2] 14ee  BS[3] 5fa0 , Prev_Value ccc3 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[1];
#X[3] = F[2];

# to : 5FA0 CCC3 9E58 14EE 
# T-Depth : 4
# Depth : 34
