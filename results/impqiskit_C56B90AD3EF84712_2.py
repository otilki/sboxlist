# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[0];
#F[2] = X[2];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 00ff  BS[2] 3c3c  BS[3] 5555 , Prev_Value 3333 , Rem Cost 1

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 00ff  BS[2] 3c3c  BS[3] aaaa , Prev_Value 5555 , Rem Cost 2

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 0cf3  BS[2] 3c3c  BS[3] aaaa , Prev_Value 00ff , Rem Cost 102

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 033f  BS[1] 0cf3  BS[2] 3c3c  BS[3] aaaa , Prev_Value 0f0f , Rem Cost 202

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 033f  BS[1] 0cf3  BS[2] 3c3c  BS[3] aaaa , Prev_Value 3e16 , Rem Cost 205 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 033f  BS[1] 0cf3  BS[2] 3e16  BS[3] aaaa , Prev_Value 32e5 , Rem Cost 105 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 033f  BS[1] 0cf3  BS[2] 32e5  BS[3] aaaa , Prev_Value f30c , Rem Cost 104 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 033f  BS[1] f30c  BS[2] 32e5  BS[3] aaaa , Prev_Value a995 , Rem Cost 103 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] a995  BS[1] f30c  BS[2] 32e5  BS[3] aaaa , Prev_Value 59a6 , Rem Cost 102 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] a995  BS[1] f30c  BS[2] 32e5  BS[3] 59a6 , Prev_Value 9b70 , Rem Cost 101 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 9b70  BS[1] f30c  BS[2] 32e5  BS[3] 59a6 , Prev_Value e16c , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[3];

# to : 9B70 E16C 32E5 59A6 
# T-Depth : 4
# Depth : 35
