# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 5555  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 100

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] 5555  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 300

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] aaaa  BS[3] f0f0 , Prev_Value 5555 , Rem Cost 400

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] aaaa  BS[3] c3c3 , Prev_Value f0f0 , Rem Cost 600

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 7788  BS[2] aaaa  BS[3] c3c3 , Prev_Value 55aa , Rem Cost 1300

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 70b3  BS[1] 7788  BS[2] aaaa  BS[3] c3c3 , Prev_Value 3333 , Rem Cost 2000

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 70b3  BS[1] 7788  BS[2] aaaa  BS[3] c3c3 , Prev_Value da2a , Rem Cost 2100 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 70b3  BS[1] 7788  BS[2] da2a  BS[3] c3c3 , Prev_Value 3c3c , Rem Cost 1400 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 70b3  BS[1] 7788  BS[2] da2a  BS[3] 3c3c , Prev_Value e616 , Rem Cost 1300 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 70b3  BS[1] 7788  BS[2] e616  BS[3] 3c3c , Prev_Value 96a5 , Rem Cost 1100 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 96a5  BS[1] 7788  BS[2] e616  BS[3] 3c3c , Prev_Value 4bb4 , Rem Cost 900 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 96a5  BS[1] 7788  BS[2] e616  BS[3] 4bb4 , Prev_Value 359c , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[2];
#X[2] = F[0];
#X[3] = F[3];

# to : 359C E616 96A5 4BB4 
# T-Depth : 4
# Depth : 35
