# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 03fc  BS[1] 3333  BS[2] 0f0f  BS[3] 5555 , Prev_Value 00ff , Rem Cost 700

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 03fc  BS[1] 3333  BS[2] 3c3c  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 900

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 03fc  BS[1] 3333  BS[2] 3d68  BS[3] 5555 , Prev_Value 3c3c , Rem Cost 1600

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 03fc  BS[1] 2673  BS[2] 3d68  BS[3] 5555 , Prev_Value 3333 , Rem Cost 2300

#circuit.cccx((1),(2),(3),(0))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 03fc  BS[1] 2673  BS[2] 3d68  BS[3] 5555 , Prev_Value 07bc , Rem Cost 3700 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 07bc  BS[1] 2673  BS[2] 3d68  BS[3] 5555 , Prev_Value 52e9 , Rem Cost 1600 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 07bc  BS[1] 2673  BS[2] 3d68  BS[3] 52e9 , Prev_Value 3ad4 , Rem Cost 1400 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 3ad4  BS[1] 2673  BS[2] 3d68  BS[3] 52e9 , Prev_Value c52b , Rem Cost 1200 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] c52b  BS[1] 2673  BS[2] 3d68  BS[3] 52e9 , Prev_Value 394b , Rem Cost 1100 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] c52b  BS[1] 2673  BS[2] 394b  BS[3] 52e9 , Prev_Value 749a , Rem Cost 400 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] c52b  BS[1] 749a  BS[2] 394b  BS[3] 52e9 , Prev_Value 97c2 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[2];

# to : 97C2 749A 52E9 394B 
# T-Depth : 7
# Depth : 60
