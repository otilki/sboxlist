# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[0];
#F[2] = X[2];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] 3333  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 100

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] 3333  BS[3] a5a5 , Prev_Value f0f0 , Rem Cost 300

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 55f0  BS[1] 00ff  BS[2] 3333  BS[3] a5a5 , Prev_Value 5555 , Rem Cost 1000

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55f0  BS[1] 00ff  BS[2] 66c3  BS[3] a5a5 , Prev_Value 3333 , Rem Cost 1200

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 55f0  BS[1] 00ff  BS[2] 66c3  BS[3] c366 , Prev_Value a5a5 , Rem Cost 1400

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 55f0  BS[1] 550f  BS[2] 66c3  BS[3] c366 , Prev_Value 00ff , Rem Cost 1600

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 14f6  BS[1] 550f  BS[2] 66c3  BS[3] c366 , Prev_Value 55f0 , Rem Cost 2300

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 14f6  BS[1] 550f  BS[2] 66c3  BS[3] c366 , Prev_Value 51cd , Rem Cost 2200 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 14f6  BS[1] 51cd  BS[2] 66c3  BS[3] c366 , Prev_Value 92ab , Rem Cost 1500 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 14f6  BS[1] 51cd  BS[2] 66c3  BS[3] 92ab , Prev_Value 7661 , Rem Cost 1300 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 14f6  BS[1] 51cd  BS[2] 7661  BS[3] 92ab , Prev_Value 453b , Rem Cost 600 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 453b  BS[1] 51cd  BS[2] 7661  BS[3] 92ab , Prev_Value 6d54 , Rem Cost 400 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 453b  BS[1] 51cd  BS[2] 7661  BS[3] 6d54 , Prev_Value 286f , Rem Cost 300 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 286f  BS[1] 51cd  BS[2] 7661  BS[3] 6d54 , Prev_Value 899e , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[0];

# to : 6D54 899E 51CD 286F 
# T-Depth : 4
# Depth : 41
