# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 6655  BS[2] 0f0f  BS[3] ff00 , Prev_Value 5555 , Rem Cost 800

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 6655  BS[2] 695a  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 1000

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 6655  BS[2] 695a  BS[3] 965a , Prev_Value ff00 , Rem Cost 1200

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 6655  BS[2] 695a  BS[3] b44b , Prev_Value 965a , Rem Cost 1900

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 6655  BS[2] 695a  BS[3] b44b , Prev_Value 1772 , Rem Cost 2000 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1772  BS[1] 6655  BS[2] 695a  BS[3] b44b , Prev_Value 96a5 , Rem Cost 1300 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1772  BS[1] 6655  BS[2] 96a5  BS[3] b44b , Prev_Value 81d7 , Rem Cost 1200 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 81d7  BS[1] 6655  BS[2] 96a5  BS[3] b44b , Prev_Value e616 , Rem Cost 1000 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 81d7  BS[1] e616  BS[2] 96a5  BS[3] b44b , Prev_Value 359c , Rem Cost 300 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 359c  BS[1] e616  BS[2] 96a5  BS[3] b44b , Prev_Value 4bb4 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[3];

# to : 359C E616 96A5 4BB4 
# T-Depth : 4
# Depth : 38
