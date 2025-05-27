# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 333c  BS[2] 5555  BS[3] 00ff , Prev_Value 3333 , Rem Cost 700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 333c  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 800

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 333c  BS[2] 5555  BS[3] ee14 , Prev_Value ff00 , Rem Cost 1500

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 333c  BS[2] 5555  BS[3] ee14 , Prev_Value 4b1b , Rem Cost 2000 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 4b1b  BS[1] 333c  BS[2] 5555  BS[3] ee14 , Prev_Value bb41 , Rem Cost 1300 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 4b1b  BS[1] 333c  BS[2] bb41  BS[3] ee14 , Prev_Value a50f , Rem Cost 1100 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 4b1b  BS[1] 333c  BS[2] bb41  BS[3] a50f , Prev_Value 9a4d , Rem Cost 900 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 4b1b  BS[1] 333c  BS[2] 9a4d  BS[3] a50f , Prev_Value 5af0 , Rem Cost 200 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 4b1b  BS[1] 333c  BS[2] 9a4d  BS[3] 5af0 , Prev_Value b4e4 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[0];

# to : 5AF0 333C 9A4D B4E4 
# T-Depth : 4
# Depth : 34
