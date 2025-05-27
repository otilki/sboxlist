# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[1];
#F[2] = X[0];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 0f0f  BS[2] 00ff  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] 0f0f  BS[2] 33cc  BS[3] 3333 , Prev_Value 00ff , Rem Cost 300

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 99aa  BS[1] 0f0f  BS[2] 33cc  BS[3] 3333 , Prev_Value aaaa , Rem Cost 1000

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 99aa  BS[1] 0f0f  BS[2] 33cc  BS[3] 3c3c , Prev_Value 3333 , Rem Cost 1200

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 99aa  BS[1] 0f0f  BS[2] aa66  BS[3] 3c3c , Prev_Value 33cc , Rem Cost 1400

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 99aa  BS[1] a569  BS[2] aa66  BS[3] 3c3c , Prev_Value 0f0f , Rem Cost 1600

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 99aa  BS[1] a569  BS[2] aa66  BS[3] b41e , Prev_Value 3c3c , Rem Cost 2300

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 99aa  BS[1] a569  BS[2] aa66  BS[3] b41e , Prev_Value 3da2 , Rem Cost 1700 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3da2  BS[1] a569  BS[2] aa66  BS[3] b41e , Prev_Value 9e64 , Rem Cost 1000 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3da2  BS[1] a569  BS[2] 9e64  BS[3] b41e , Prev_Value 89bc , Rem Cost 300 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3da2  BS[1] a569  BS[2] 9e64  BS[3] 89bc , Prev_Value 5a96 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[2];
#X[2] = F[0];
#X[3] = F[3];

# to : 5A96 9E64 3DA2 89BC 
# T-Depth : 4
# Depth : 36
