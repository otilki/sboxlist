# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 3333  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 3333  BS[3] ee11 , Prev_Value ff00 , Rem Cost 800

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 7722  BS[3] ee11 , Prev_Value 3333 , Rem Cost 1500

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 5a5a  BS[2] 7722  BS[3] ee11 , Prev_Value 5555 , Rem Cost 1700

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5a5a  BS[2] 9933  BS[3] ee11 , Prev_Value 7722 , Rem Cost 1900

#circuit.cccx((0),(2),(3),(1))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 525b  BS[2] 9933  BS[3] ee11 , Prev_Value 5a5a , Rem Cost 4000

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 525b  BS[2] 9933  BS[3] ee11 , Prev_Value 1f1c , Rem Cost 2600 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 1f1c  BS[1] 525b  BS[2] 9933  BS[3] ee11 , Prev_Value 862f , Rem Cost 1900 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 1f1c  BS[1] 525b  BS[2] 862f  BS[3] ee11 , Prev_Value bc4a , Rem Cost 1700 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1f1c  BS[1] bc4a  BS[2] 862f  BS[3] ee11 , Prev_Value 683e , Rem Cost 1500 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1f1c  BS[1] bc4a  BS[2] 862f  BS[3] 683e , Prev_Value 9a27 , Rem Cost 1300 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1f1c  BS[1] bc4a  BS[2] 9a27  BS[3] 683e , Prev_Value a356 , Rem Cost 600 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] a356  BS[1] bc4a  BS[2] 9a27  BS[3] 683e , Prev_Value 266d , Rem Cost 400 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] a356  BS[1] 266d  BS[2] 9a27  BS[3] 683e , Prev_Value 5ca9 , Rem Cost 200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 5ca9  BS[1] 266d  BS[2] 9a27  BS[3] 683e , Prev_Value 65d8 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[0];

# to : 266D 683E 65D8 5CA9 
# T-Depth : 7
# Depth : 61
