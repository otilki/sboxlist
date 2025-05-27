# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 3333  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3333  BS[3] f0f0 , Prev_Value 5555 , Rem Cost 2

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] cccc  BS[3] f0f0 , Prev_Value 3333 , Rem Cost 3

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] ff00  BS[1] aaaa  BS[2] cccc  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 4

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] ff00  BS[1] 5aaa  BS[2] cccc  BS[3] f0f0 , Prev_Value aaaa , Rem Cost 104

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3fc0  BS[1] 5aaa  BS[2] cccc  BS[3] f0f0 , Prev_Value ff00 , Rem Cost 204

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3fc0  BS[1] 5aaa  BS[2] cccc  BS[3] f0f0 , Prev_Value b878 , Rem Cost 204 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3fc0  BS[1] 5aaa  BS[2] cccc  BS[3] b878 , Prev_Value d64c , Rem Cost 104 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3fc0  BS[1] 5aaa  BS[2] d64c  BS[3] b878 , Prev_Value 4787 , Rem Cost 4 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3fc0  BS[1] 5aaa  BS[2] d64c  BS[3] 4787 , Prev_Value 29b3 , Rem Cost 3 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3fc0  BS[1] 5aaa  BS[2] 29b3  BS[3] 4787 , Prev_Value a555 , Rem Cost 2 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 3fc0  BS[1] a555  BS[2] 29b3  BS[3] 4787 , Prev_Value c03f , Rem Cost 1 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[0];
#X[2] = F[3];
#X[3] = F[2];

# to : A555 C03F 4787 29B3 
# T-Depth : 4
# Depth : 30
