# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] aaaa  BS[2] 0f0f  BS[3] 00ff , Prev_Value 5555 , Rem Cost 100

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] aaaa  BS[2] 0f0f  BS[3] 03fc , Prev_Value 00ff , Rem Cost 800

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] aaaa  BS[2] f0f0  BS[3] 03fc , Prev_Value 0f0f , Rem Cost 900

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] cccc  BS[1] aaaa  BS[2] f0f0  BS[3] 03fc , Prev_Value 3333 , Rem Cost 1000

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] cccc  BS[1] aaaa  BS[2] f0f0  BS[3] fc03 , Prev_Value 03fc , Rem Cost 1100

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] f0f0  BS[3] fc03 , Prev_Value cccc , Rem Cost 1800

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] f0f0  BS[3] fc03 , Prev_Value 58f2 , Rem Cost 2000 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] 58f2  BS[3] fc03 , Prev_Value 349e , Rem Cost 1300 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] 349e  BS[3] fc03 , Prev_Value 56a9 , Rem Cost 1100 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 6c6c  BS[1] 56a9  BS[2] 349e  BS[3] fc03 , Prev_Value 6237 , Rem Cost 900 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6c6c  BS[1] 6237  BS[2] 349e  BS[3] fc03 , Prev_Value 589e , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[1];

# to : 6C6C FC03 589E 6237 
# T-Depth : 4
# Depth : 33
