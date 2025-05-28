# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3333  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] cccc  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 200

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] cccc  BS[3] c3c3 , Prev_Value 0f0f , Rem Cost 400

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6a6a  BS[2] cccc  BS[3] c3c3 , Prev_Value aaaa , Rem Cost 1100

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 6a6a  BS[2] a6a6  BS[3] c3c3 , Prev_Value cccc , Rem Cost 1300

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 6a6a  BS[2] a6a6  BS[3] c33c , Prev_Value c3c3 , Rem Cost 1500

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6a56  BS[2] a6a6  BS[3] c33c , Prev_Value 6a6a , Rem Cost 2200

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 6a56  BS[2] a6a6  BS[3] c33c , Prev_Value 22f9 , Rem Cost 2000 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 22f9  BS[1] 6a56  BS[2] a6a6  BS[3] c33c , Prev_Value 659a , Rem Cost 1300 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 22f9  BS[1] 6a56  BS[2] 659a  BS[3] c33c , Prev_Value e16c , Rem Cost 1100 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 22f9  BS[1] 6a56  BS[2] 659a  BS[3] e16c , Prev_Value c395 , Rem Cost 400 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] c395  BS[1] 6a56  BS[2] 659a  BS[3] e16c , Prev_Value a9c3 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[1];
#X[3] = F[2];

# to : E16C C395 A9C3 659A 
# T-Depth : 4
# Depth : 39
