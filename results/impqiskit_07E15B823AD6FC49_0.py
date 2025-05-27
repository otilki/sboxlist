# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 5555  BS[3] 11ee , Prev_Value 00ff , Rem Cost 700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] aaaa  BS[3] 11ee , Prev_Value 5555 , Rem Cost 800

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] aaaa  BS[3] ee11 , Prev_Value 11ee , Rem Cost 900

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 9933  BS[2] aaaa  BS[3] ee11 , Prev_Value 3333 , Rem Cost 1600

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 9933  BS[2] a5a5  BS[3] ee11 , Prev_Value aaaa , Rem Cost 1800

#circuit.cccx((0),(1),(3),(2))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 9933  BS[2] ada4  BS[3] ee11 , Prev_Value a5a5 , Rem Cost 3900

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 9933  BS[2] ada4  BS[3] ee11 , Prev_Value 862f , Rem Cost 2500 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 862f  BS[1] 9933  BS[2] ada4  BS[3] ee11 , Prev_Value 43b5 , Rem Cost 1800 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 862f  BS[1] 9933  BS[2] ada4  BS[3] 43b5 , Prev_Value c59a , Rem Cost 1600 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] c59a  BS[1] 9933  BS[2] ada4  BS[3] 43b5 , Prev_Value 683e , Rem Cost 1400 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] c59a  BS[1] 9933  BS[2] 683e  BS[3] 43b5 , Prev_Value 5ca9 , Rem Cost 1200 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 5ca9  BS[1] 9933  BS[2] 683e  BS[3] 43b5 , Prev_Value d992 , Rem Cost 1000 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 5ca9  BS[1] d992  BS[2] 683e  BS[3] 43b5 , Prev_Value 266d , Rem Cost 300 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5ca9  BS[1] 266d  BS[2] 683e  BS[3] 43b5 , Prev_Value 65d8 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[2];
#X[2] = F[3];
#X[3] = F[0];

# to : 266D 683E 65D8 5CA9 
# T-Depth : 7
# Depth : 63
