# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 3636  BS[2] 5555  BS[3] ff00 , Prev_Value 3333 , Rem Cost 800

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3636  BS[2] 6355  BS[3] ff00 , Prev_Value 5555 , Rem Cost 1500

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3636  BS[2] 6355  BS[3] 9c55 , Prev_Value ff00 , Rem Cost 1700

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3636  BS[2] 6c5a  BS[3] 9c55 , Prev_Value 6355 , Rem Cost 1900

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 035f  BS[1] 3636  BS[2] 6c5a  BS[3] 9c55 , Prev_Value 0f0f , Rem Cost 2600

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 035f  BS[1] 3636  BS[2] 6c5a  BS[3] 9c55 , Prev_Value 9e43 , Rem Cost 2300 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 035f  BS[1] 3636  BS[2] 6c5a  BS[3] 9e43 , Prev_Value 6f05 , Rem Cost 1600 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6f05  BS[1] 3636  BS[2] 6c5a  BS[3] 9e43 , Prev_Value f219 , Rem Cost 1400 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 6f05  BS[1] 3636  BS[2] f219  BS[3] 9e43 , Prev_Value 90fa , Rem Cost 1200 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 90fa  BS[1] 3636  BS[2] f219  BS[3] 9e43 , Prev_Value a674 , Rem Cost 1100 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 90fa  BS[1] a674  BS[2] f219  BS[3] 9e43 , Prev_Value 368e , Rem Cost 400 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 368e  BS[1] a674  BS[2] f219  BS[3] 9e43 , Prev_Value c497 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[3];

# to : 368E C497 A674 9E43 
# T-Depth : 5
# Depth : 47
