# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 3c3c  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 300

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 693c  BS[3] ff00 , Prev_Value 3c3c , Rem Cost 1000

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 7465  BS[1] 3333  BS[2] 693c  BS[3] ff00 , Prev_Value 5555 , Rem Cost 1700

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 7465  BS[1] 3333  BS[2] 693c  BS[3] 8b65 , Prev_Value ff00 , Rem Cost 1900

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 693c  BS[3] 8b65 , Prev_Value 7465 , Rem Cost 2100

#circuit.cccx((0),(1),(3),(2))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 693c  BS[3] 8b65 , Prev_Value 683d , Rem Cost 3900 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 683d  BS[3] 8b65 , Prev_Value 97c2 , Rem Cost 1800 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 97c2  BS[3] 8b65 , Prev_Value 2673 , Rem Cost 1700 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 1d59  BS[1] 2673  BS[2] 97c2  BS[3] 8b65 , Prev_Value 749a , Rem Cost 1000 R

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 1d59  BS[1] 2673  BS[2] 97c2  BS[3] 749a , Prev_Value 394b , Rem Cost 900 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 394b  BS[1] 2673  BS[2] 97c2  BS[3] 749a , Prev_Value 52e9 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : 97C2 749A 52E9 394B 
# T-Depth : 7
# Depth : 58
