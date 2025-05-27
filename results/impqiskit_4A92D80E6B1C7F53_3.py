# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[1];
#F[2] = X[0];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] ff00  BS[3] 5555 , Prev_Value 00ff , Rem Cost 100

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] ff00  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 300

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] ff00  BS[3] aaaa , Prev_Value 5555 , Rem Cost 400

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] cc33  BS[1] 5a5a  BS[2] ff00  BS[3] aaaa , Prev_Value 3333 , Rem Cost 600

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] cc33  BS[1] 5a5a  BS[2] ff00  BS[3] f0aa , Prev_Value aaaa , Rem Cost 1300

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] cc33  BS[1] 9669  BS[2] ff00  BS[3] f0aa , Prev_Value 5a5a , Rem Cost 1500

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c99  BS[1] 9669  BS[2] ff00  BS[3] f0aa , Prev_Value cc33 , Rem Cost 1700

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3c99  BS[1] 9669  BS[2] eb09  BS[3] f0aa , Prev_Value ff00 , Rem Cost 2400

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c99  BS[1] 9669  BS[2] eb09  BS[3] f0aa , Prev_Value 7661 , Rem Cost 2100 R

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3c99  BS[1] 7661  BS[2] eb09  BS[3] f0aa , Prev_Value 92ab , Rem Cost 1400 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c99  BS[1] 7661  BS[2] eb09  BS[3] 92ab , Prev_Value d790 , Rem Cost 700 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3c99  BS[1] 7661  BS[2] d790  BS[3] 92ab , Prev_Value 899e , Rem Cost 500 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c99  BS[1] 899e  BS[2] d790  BS[3] 92ab , Prev_Value 286f , Rem Cost 400 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c99  BS[1] 899e  BS[2] 286f  BS[3] 92ab , Prev_Value 6d54 , Rem Cost 300 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c99  BS[1] 899e  BS[2] 286f  BS[3] 6d54 , Prev_Value 51cd , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[0];
#X[3] = F[2];

# to : 6D54 899E 51CD 286F 
# T-Depth : 4
# Depth : 39
