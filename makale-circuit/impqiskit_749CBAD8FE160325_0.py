# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 555a  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 700

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 0ff0  BS[2] 555a  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 900

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 0ff0  BS[2] 555a  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1000

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 3fc0  BS[2] 555a  BS[3] f0f0 , Prev_Value 0ff0 , Rem Cost 1700

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 3fc0  BS[2] 555a  BS[3] f0f0 , Prev_Value 2673 , Rem Cost 1700 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 3fc0  BS[2] 555a  BS[3] f0f0 , Prev_Value aaa5 , Rem Cost 1000 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 2673  BS[1] 3fc0  BS[2] aaa5  BS[3] f0f0 , Prev_Value d2d1 , Rem Cost 900 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2673  BS[1] 3fc0  BS[2] aaa5  BS[3] d2d1 , Prev_Value 8cd6 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[2];

# to : 3FC0 D2D1 8CD6 AAA5 
# T-Depth : 4
# Depth : 34
