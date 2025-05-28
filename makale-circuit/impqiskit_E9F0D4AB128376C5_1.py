# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[0];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] cccc  BS[1] 5555  BS[2] 00ff  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 100

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] cccc  BS[1] 5555  BS[2] ff00  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 200

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] cccc  BS[1] 5555  BS[2] ff00  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 300

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3ccc  BS[1] 5555  BS[2] ff00  BS[3] f0f0 , Prev_Value cccc , Rem Cost 1000

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3ccc  BS[1] 5555  BS[2] aa55  BS[3] f0f0 , Prev_Value ff00 , Rem Cost 1200

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3ccc  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value 5555 , Rem Cost 1400

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 14dd  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value 3ccc , Rem Cost 2100

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 14dd  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value eb22 , Rem Cost 1600 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] eb22  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1500 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] eb22  BS[1] 6999  BS[2] aa55  BS[3] 0f0f , Prev_Value a35c , Rem Cost 1400 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] eb22  BS[1] 6999  BS[2] a35c  BS[3] 0f0f , Prev_Value ac0f , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[1];

# to : EB22 AC0F A35C 6999 
# T-Depth : 4
# Depth : 33
