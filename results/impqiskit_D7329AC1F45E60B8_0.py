# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5555  BS[3] 00ff , Prev_Value 3333 , Rem Cost 200

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5599  BS[3] 00ff , Prev_Value 5555 , Rem Cost 900

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5599  BS[3] 05f6 , Prev_Value 00ff , Rem Cost 1600

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 506f  BS[3] 05f6 , Prev_Value 5599 , Rem Cost 1800

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 506f  BS[3] fa09 , Prev_Value 05f6 , Rem Cost 1900

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value 506f , Rem Cost 2100

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value 3d07 , Rem Cost 2500 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 3d07  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value c2f8 , Rem Cost 1800 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] c2f8  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value 716c , Rem Cost 1700 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] c2f8  BS[1] 716c  BS[2] 63a3  BS[3] fa09 , Prev_Value 8e93 , Rem Cost 1000 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] c2f8  BS[1] 8e93  BS[2] 63a3  BS[3] fa09 , Prev_Value e9a2 , Rem Cost 900 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] c2f8  BS[1] 8e93  BS[2] e9a2  BS[3] fa09 , Prev_Value 749a , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[0];
#X[2] = F[3];
#X[3] = F[2];

# to : 8E93 C2F8 749A E9A2 
# T-Depth : 5
# Depth : 45
