# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] cccc , Prev_Value 3333 , Rem Cost 100

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] c9c9 , Prev_Value cccc , Rem Cost 800

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 55aa  BS[3] c9c9 , Prev_Value 5555 , Rem Cost 1000

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 0ff0  BS[2] 55aa  BS[3] c9c9 , Prev_Value 0f0f , Rem Cost 1200

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0ff0  BS[2] 5563  BS[3] c9c9 , Prev_Value 55aa , Rem Cost 1900

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 0ff0  BS[2] 5563  BS[3] c9c9 , Prev_Value 4eb1 , Rem Cost 1900 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 4eb1  BS[2] 5563  BS[3] c9c9 , Prev_Value 44de , Rem Cost 1200 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 44de  BS[1] 4eb1  BS[2] 5563  BS[3] c9c9 , Prev_Value 8778 , Rem Cost 500 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 44de  BS[1] 4eb1  BS[2] 5563  BS[3] 8778 , Prev_Value c3a6 , Rem Cost 300 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] c3a6  BS[1] 4eb1  BS[2] 5563  BS[3] 8778 , Prev_Value 3c59 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[0];
#X[2] = F[1];
#X[3] = F[3];

# to : 5563 3C59 4EB1 8778 
# T-Depth : 4
# Depth : 38
