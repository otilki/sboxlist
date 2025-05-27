# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[0];
#F[2] = X[2];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 00ff  BS[2] cccc  BS[3] 5555 , Prev_Value 3333 , Rem Cost 100

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] cccc  BS[3] 5555 , Prev_Value 00ff , Rem Cost 800

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] 8877  BS[3] 5555 , Prev_Value cccc , Rem Cost 1000

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] 8877  BS[3] dd22 , Prev_Value 5555 , Rem Cost 1200

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f3c  BS[1] 44bb  BS[2] 8877  BS[3] dd22 , Prev_Value 0f0f , Rem Cost 1900

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f3c  BS[1] 44bb  BS[2] 8877  BS[3] dd22 , Prev_Value d516 , Rem Cost 1800 R

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f3c  BS[1] 44bb  BS[2] 8877  BS[3] d516 , Prev_Value 41af , Rem Cost 1100 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f3c  BS[1] 41af  BS[2] 8877  BS[3] d516 , Prev_Value 94b9 , Rem Cost 400 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f3c  BS[1] 41af  BS[2] 8877  BS[3] 94b9 , Prev_Value 7788 , Rem Cost 200 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 0f3c  BS[1] 41af  BS[2] 7788  BS[3] 94b9 , Prev_Value be50 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[0];
#X[2] = F[3];
#X[3] = F[1];

# to : 7788 0F3C 94B9 BE50 
# T-Depth : 4
# Depth : 36
