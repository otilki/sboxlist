# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 3636 , Prev_Value 3333 , Rem Cost 700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aaaa  BS[3] 3636 , Prev_Value 5555 , Rem Cost 800

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aa9c  BS[3] 3636 , Prev_Value aaaa , Rem Cost 1500

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aa9c  BS[3] c9c9 , Prev_Value 3636 , Rem Cost 1600

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aa9c  BS[3] c9c9 , Prev_Value 8787 , Rem Cost 2000 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 8787  BS[2] aa9c  BS[3] c9c9 , Prev_Value 8778 , Rem Cost 1300 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 8778  BS[1] 8787  BS[2] aa9c  BS[3] c9c9 , Prev_Value 4eb1 , Rem Cost 1100 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 8778  BS[1] 8787  BS[2] aa9c  BS[3] 4eb1 , Prev_Value 7878 , Rem Cost 900 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 8778  BS[1] 7878  BS[2] aa9c  BS[3] 4eb1 , Prev_Value 5563 , Rem Cost 800 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 8778  BS[1] 7878  BS[2] 5563  BS[3] 4eb1 , Prev_Value 3c59 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[0];

# to : 5563 3C59 4EB1 8778 
# T-Depth : 4
# Depth : 34
