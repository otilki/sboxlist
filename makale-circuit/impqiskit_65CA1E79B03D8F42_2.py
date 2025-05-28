# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 5566  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5566  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 800

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 5566  BS[2] 0f0f  BS[3] cccc , Prev_Value 00ff , Rem Cost 1000

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0ff0  BS[1] 5566  BS[2] c3c3  BS[3] cccc , Prev_Value 0f0f , Rem Cost 1200

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 4bb4  BS[1] 5566  BS[2] c3c3  BS[3] cccc , Prev_Value 0ff0 , Rem Cost 1900

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 5566  BS[2] c3c3  BS[3] cccc , Prev_Value 8f4c , Rem Cost 2000 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 5566  BS[2] c3c3  BS[3] 8f4c , Prev_Value 96a5 , Rem Cost 1300 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] c3c3  BS[3] 8f4c , Prev_Value 19e9 , Rem Cost 1100 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] c3c3  BS[3] 19e9 , Prev_Value ca63 , Rem Cost 900 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] ca63  BS[3] 19e9 , Prev_Value 359c , Rem Cost 200 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] 359c  BS[3] 19e9 , Prev_Value e616 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : 359C E616 96A5 4BB4 
# T-Depth : 4
# Depth : 37
