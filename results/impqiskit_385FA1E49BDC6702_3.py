# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 333c  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 333c  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 800

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 11eb  BS[1] 5555  BS[2] 333c  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 1500

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 11eb  BS[1] 5555  BS[2] ccc3  BS[3] f0f0 , Prev_Value 333c , Rem Cost 1600

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 11eb  BS[1] 5555  BS[2] ccc3  BS[3] f0f0 , Prev_Value e1b1 , Rem Cost 2100 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 11eb  BS[1] 5555  BS[2] ccc3  BS[3] e1b1 , Prev_Value b4e4 , Rem Cost 1400 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 11eb  BS[1] b4e4  BS[2] ccc3  BS[3] e1b1 , Prev_Value a50f , Rem Cost 1200 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] a50f  BS[1] b4e4  BS[2] ccc3  BS[3] e1b1 , Prev_Value 65b2 , Rem Cost 1000 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] a50f  BS[1] b4e4  BS[2] ccc3  BS[3] 65b2 , Prev_Value 333c , Rem Cost 300 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] a50f  BS[1] b4e4  BS[2] 333c  BS[3] 65b2 , Prev_Value 5af0 , Rem Cost 200 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5af0  BS[1] b4e4  BS[2] 333c  BS[3] 65b2 , Prev_Value 9a4d , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[3];
#X[3] = F[1];

# to : 5AF0 333C 9A4D B4E4 
# T-Depth : 4
# Depth : 33
