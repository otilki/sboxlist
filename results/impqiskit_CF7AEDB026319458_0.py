# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] 0f0f  BS[3] 00ff , Prev_Value 5555 , Rem Cost 200

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 300

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] f0f0  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 400

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] a5f0  BS[3] ff00 , Prev_Value f0f0 , Rem Cost 1100

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 749a  BS[2] a5f0  BS[3] ff00 , Prev_Value 55aa , Rem Cost 1800

#circuit.cccx((0),(1),(2),(3))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 749a  BS[2] a5f0  BS[3] df10 , Prev_Value ff00 , Rem Cost 3900

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 749a  BS[2] a5f0  BS[3] df10 , Prev_Value 6723 , Rem Cost 2300 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6723  BS[1] 749a  BS[2] a5f0  BS[3] df10 , Prev_Value 7ae0 , Rem Cost 1600 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 6723  BS[1] 749a  BS[2] 7ae0  BS[3] df10 , Prev_Value b833 , Rem Cost 1400 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 6723  BS[1] 749a  BS[2] 7ae0  BS[3] b833 , Prev_Value 13b9 , Rem Cost 1200 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 13b9  BS[1] 749a  BS[2] 7ae0  BS[3] b833 , Prev_Value 663a , Rem Cost 1000 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 13b9  BS[1] 663a  BS[2] 7ae0  BS[3] b833 , Prev_Value de09 , Rem Cost 300 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 13b9  BS[1] 663a  BS[2] 7ae0  BS[3] de09 , Prev_Value ec46 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[2];
#X[3] = F[1];

# to : DE09 EC46 7AE0 663A 
# T-Depth : 7
# Depth : 60
