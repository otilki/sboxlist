# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 6666  BS[3] 3333 , Prev_Value 5555 , Rem Cost 200

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6666  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 400

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6666  BS[3] cccc , Prev_Value 3333 , Rem Cost 500

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6666  BS[3] cc33 , Prev_Value cccc , Rem Cost 700

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6a56  BS[3] cc33 , Prev_Value 6666 , Rem Cost 1400

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 3c6a  BS[2] 6a56  BS[3] cc33 , Prev_Value 3c3c , Rem Cost 2100

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c6a  BS[2] 6a56  BS[3] cc33 , Prev_Value cc59 , Rem Cost 2100 R

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 3c6a  BS[2] 6a56  BS[3] cc59 , Prev_Value 48af , Rem Cost 1400 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 48af  BS[1] 3c6a  BS[2] 6a56  BS[3] cc59 , Prev_Value c395 , Rem Cost 700 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 48af  BS[1] c395  BS[2] 6a56  BS[3] cc59 , Prev_Value a9c3 , Rem Cost 600 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 48af  BS[1] c395  BS[2] a9c3  BS[3] cc59 , Prev_Value 659a , Rem Cost 400 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 48af  BS[1] c395  BS[2] a9c3  BS[3] 659a , Prev_Value e16c , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[3];

# to : E16C C395 A9C3 659A 
# T-Depth : 4
# Depth : 41
