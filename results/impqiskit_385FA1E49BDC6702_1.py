# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 0f0f  BS[3] aaaa , Prev_Value 5555 , Rem Cost 100

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 333c  BS[2] 0f0f  BS[3] aaaa , Prev_Value 3333 , Rem Cost 800

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 33c3  BS[1] 333c  BS[2] 0f0f  BS[3] aaaa , Prev_Value 00ff , Rem Cost 1000

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 33c3  BS[1] 333c  BS[2] a5a5  BS[3] aaaa , Prev_Value 0f0f , Rem Cost 1200

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 11eb  BS[1] 333c  BS[2] a5a5  BS[3] aaaa , Prev_Value 33c3 , Rem Cost 1900

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 11eb  BS[1] 333c  BS[2] a5a5  BS[3] aaaa , Prev_Value a50f , Rem Cost 1900 R

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 11eb  BS[1] 333c  BS[2] a50f  BS[3] aaaa , Prev_Value 8ba6 , Rem Cost 1200 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 11eb  BS[1] 333c  BS[2] a50f  BS[3] 8ba6 , Prev_Value 9a4d , Rem Cost 500 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 11eb  BS[1] 333c  BS[2] a50f  BS[3] 9a4d , Prev_Value b4e4 , Rem Cost 300 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] b4e4  BS[1] 333c  BS[2] a50f  BS[3] 9a4d , Prev_Value 5af0 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[0];

# to : 5AF0 333C 9A4D B4E4 
# T-Depth : 4
# Depth : 35
