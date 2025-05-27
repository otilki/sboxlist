# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 5555  BS[3] 05fa , Prev_Value 00ff , Rem Cost 700

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 5467  BS[3] 05fa , Prev_Value 5555 , Rem Cost 1400

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 5467  BS[3] fa05 , Prev_Value 05fa , Rem Cost 1500

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 5b68  BS[1] 3333  BS[2] 5467  BS[3] fa05 , Prev_Value 0f0f , Rem Cost 1700

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5b68  BS[1] 3333  BS[2] ae62  BS[3] fa05 , Prev_Value 5467 , Rem Cost 1900

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 5b68  BS[1] 685b  BS[2] ae62  BS[3] fa05 , Prev_Value 3333 , Rem Cost 2100

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 5b68  BS[1] 685b  BS[2] ae62  BS[3] fa05 , Prev_Value f168 , Rem Cost 2000 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] f168  BS[1] 685b  BS[2] ae62  BS[3] fa05 , Prev_Value 9a4d , Rem Cost 1300 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] f168  BS[1] 685b  BS[2] ae62  BS[3] 9a4d , Prev_Value 6b25 , Rem Cost 600 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 6b25  BS[1] 685b  BS[2] ae62  BS[3] 9a4d , Prev_Value 97a4 , Rem Cost 400 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6b25  BS[1] 97a4  BS[2] ae62  BS[3] 9a4d , Prev_Value 39c6 , Rem Cost 300 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 6b25  BS[1] 97a4  BS[2] 39c6  BS[3] 9a4d , Prev_Value 65b2 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[2];

# to : 97A4 65B2 6B25 39C6 
# T-Depth : 4
# Depth : 35
