# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[1];
#F[2] = X[0];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] 03fc  BS[3] 5555 , Prev_Value 00ff , Rem Cost 700

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3267  BS[1] 0f0f  BS[2] 03fc  BS[3] 5555 , Prev_Value 3333 , Rem Cost 1400

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3267  BS[1] 3d68  BS[2] 03fc  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 1600

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3267  BS[1] 3d68  BS[2] 3e94  BS[3] 5555 , Prev_Value 03fc , Rem Cost 1800

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3e94  BS[3] 5555 , Prev_Value 3267 , Rem Cost 2500

#circuit.cccx((0),(1),(3),(2))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3e94  BS[3] 5555 , Prev_Value 3ad4 , Rem Cost 3600 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3ad4  BS[3] 5555 , Prev_Value 683d , Rem Cost 1500 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3ad4  BS[3] 683d , Prev_Value 97c2 , Rem Cost 1300 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3ad4  BS[3] 97c2 , Prev_Value c52b , Rem Cost 1200 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] c52b  BS[3] 97c2 , Prev_Value 394b , Rem Cost 1100 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 394b  BS[2] c52b  BS[3] 97c2 , Prev_Value 52e9 , Rem Cost 400 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2673  BS[1] 394b  BS[2] 52e9  BS[3] 97c2 , Prev_Value 749a , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[2];
#X[3] = F[1];

# to : 97C2 749A 52E9 394B 
# T-Depth : 7
# Depth : 59
