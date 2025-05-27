# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[0];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 00ff  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] ff00  BS[2] 0f0f  BS[3] 3333 , Prev_Value 00ff , Rem Cost 200

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] ff00  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 300

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] ff00  BS[2] a50f  BS[3] cccc , Prev_Value 0f0f , Rem Cost 1000

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] 7788  BS[2] a50f  BS[3] cccc , Prev_Value ff00 , Rem Cost 1700

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 5555  BS[1] 7788  BS[2] a50f  BS[3] cccc , Prev_Value aaaa , Rem Cost 1800

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 7788  BS[2] a50f  BS[3] e9c4 , Prev_Value cccc , Rem Cost 2500

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 5555  BS[1] 7788  BS[2] a50f  BS[3] e9c4 , Prev_Value 22dd , Rem Cost 1900 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 5555  BS[1] 22dd  BS[2] a50f  BS[3] e9c4 , Prev_Value f05a , Rem Cost 1700 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] f05a  BS[1] 22dd  BS[2] a50f  BS[3] e9c4 , Prev_Value cb19 , Rem Cost 1500 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] f05a  BS[1] 22dd  BS[2] a50f  BS[3] cb19 , Prev_Value 6517 , Rem Cost 1300 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] f05a  BS[1] 22dd  BS[2] 6517  BS[3] cb19 , Prev_Value 47ca , Rem Cost 600 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] f05a  BS[1] 47ca  BS[2] 6517  BS[3] cb19 , Prev_Value 3b43 , Rem Cost 400 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3b43  BS[1] 47ca  BS[2] 6517  BS[3] cb19 , Prev_Value 9ae8 , Rem Cost 200 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 3b43  BS[1] 47ca  BS[2] 9ae8  BS[3] cb19 , Prev_Value c4bc , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[2];

# to : C4BC CB19 47CA 9AE8 
# T-Depth : 4
# Depth : 36
