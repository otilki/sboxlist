# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 200

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] a6a6  BS[2] 0f0f  BS[3] cccc , Prev_Value aaaa , Rem Cost 900

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] a6a6  BS[2] c3c3  BS[3] cccc , Prev_Value 0f0f , Rem Cost 1100

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] a659  BS[2] c3c3  BS[3] cccc , Prev_Value a6a6 , Rem Cost 1300

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] a659  BS[2] c3c3  BS[3] cc0f , Prev_Value cccc , Rem Cost 2000

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] a659  BS[2] c3c3  BS[3] cc0f , Prev_Value 84f6 , Rem Cost 2200 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 84f6  BS[1] a659  BS[2] c3c3  BS[3] cc0f , Prev_Value 6a56 , Rem Cost 1500 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 84f6  BS[1] a659  BS[2] c3c3  BS[3] 6a56 , Prev_Value 659a , Rem Cost 1300 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 84f6  BS[1] 659a  BS[2] c3c3  BS[3] 6a56 , Prev_Value c395 , Rem Cost 1100 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 84f6  BS[1] 659a  BS[2] c395  BS[3] 6a56 , Prev_Value e16c , Rem Cost 400 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] e16c  BS[1] 659a  BS[2] c395  BS[3] 6a56 , Prev_Value a9c3 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[3];
#X[3] = F[1];

# to : E16C C395 A9C3 659A 
# T-Depth : 4
# Depth : 37
