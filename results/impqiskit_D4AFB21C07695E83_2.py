# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[0];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 5555  BS[2] 00ff  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 200

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 5959  BS[2] 00ff  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 900

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 5959  BS[2] 00ff  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1000

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] 00ff  BS[3] f0f0 , Prev_Value 3c3c , Rem Cost 1700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] ff00  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 1800

#circuit.cccx((0),(1),(3),(2))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] ef40  BS[3] f0f0 , Prev_Value ff00 , Rem Cost 3900

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] ef40  BS[3] f0f0 , Prev_Value b619 , Rem Cost 2100 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] b619  BS[2] ef40  BS[3] f0f0 , Prev_Value 46e9 , Rem Cost 1900 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] b619  BS[2] ef40  BS[3] 46e9 , Prev_Value 9a59 , Rem Cost 1700 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 9a59  BS[2] ef40  BS[3] 46e9 , Prev_Value ed09 , Rem Cost 1000 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 9a59  BS[2] ed09  BS[3] 46e9 , Prev_Value d16c , Rem Cost 300 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] 9a59  BS[2] d16c  BS[3] 46e9 , Prev_Value b916 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[2];
#X[2] = F[0];
#X[3] = F[1];

# to : B916 D16C 3C65 9A59 
# T-Depth : 7
# Depth : 58
