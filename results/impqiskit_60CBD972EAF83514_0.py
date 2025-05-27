# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] cccc  BS[2] 5555  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 100

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] cccc  BS[2] 5555  BS[3] c3c3 , Prev_Value 0f0f , Rem Cost 300

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] cccc  BS[2] 5555  BS[3] c30f , Prev_Value c3c3 , Rem Cost 1000

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 5555  BS[3] c30f , Prev_Value cccc , Rem Cost 1100

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] c30f , Prev_Value 5555 , Rem Cost 1200

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaa5  BS[3] c30f , Prev_Value aaaa , Rem Cost 1900

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaa5  BS[3] c30f , Prev_Value 22de , Rem Cost 1900 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 22de  BS[1] 3333  BS[2] aaa5  BS[3] c30f , Prev_Value b136 , Rem Cost 1200 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 22de  BS[1] b136  BS[2] aaa5  BS[3] c30f , Prev_Value 93e8 , Rem Cost 500 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 22de  BS[1] 93e8  BS[2] aaa5  BS[3] c30f , Prev_Value 3cf0 , Rem Cost 300 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 22de  BS[1] 93e8  BS[2] aaa5  BS[3] 3cf0 , Prev_Value 1e2e , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[0];

# to : 3CF0 AAA5 93E8 1E2E 
# T-Depth : 4
# Depth : 35
