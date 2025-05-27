# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5555  BS[3] 00ff , Prev_Value 3333 , Rem Cost 700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 800

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5555  BS[3] fc06 , Prev_Value ff00 , Rem Cost 1500

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5555  BS[3] fc06 , Prev_Value 5953 , Rem Cost 2000 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5953  BS[3] fc06 , Prev_Value f309 , Rem Cost 1300 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] f309  BS[1] 3366  BS[2] 5953  BS[3] fc06 , Prev_Value a555 , Rem Cost 1100 R

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] f309  BS[1] 3366  BS[2] 5953  BS[3] a555 , Prev_Value d24d , Rem Cost 900 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] d24d  BS[1] 3366  BS[2] 5953  BS[3] a555 , Prev_Value 5aaa , Rem Cost 200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] d24d  BS[1] 3366  BS[2] 5953  BS[3] 5aaa , Prev_Value a6ac , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[0];
#X[3] = F[2];

# to : 5AAA 3366 D24D A6AC 
# T-Depth : 4
# Depth : 34
