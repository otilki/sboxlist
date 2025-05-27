# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] cccc  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] cccc  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 200

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 44bb  BS[1] 5555  BS[2] cccc  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 900

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 44bb  BS[1] 5555  BS[2] 8877  BS[3] f0f0 , Prev_Value cccc , Rem Cost 1100

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 44bb  BS[1] 5555  BS[2] 8877  BS[3] f0c3 , Prev_Value f0f0 , Rem Cost 1800

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 44bb  BS[1] 5555  BS[2] 8877  BS[3] f0c3 , Prev_Value d516 , Rem Cost 1900 R

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 44bb  BS[1] d516  BS[2] 8877  BS[3] f0c3 , Prev_Value 94b9 , Rem Cost 1200 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 94b9  BS[1] d516  BS[2] 8877  BS[3] f0c3 , Prev_Value 41af , Rem Cost 500 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 94b9  BS[1] 41af  BS[2] 8877  BS[3] f0c3 , Prev_Value be50 , Rem Cost 300 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 94b9  BS[1] be50  BS[2] 8877  BS[3] f0c3 , Prev_Value 0f3c , Rem Cost 200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 94b9  BS[1] be50  BS[2] 8877  BS[3] 0f3c , Prev_Value 7788 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[1];

# to : 7788 0F3C 94B9 BE50 
# T-Depth : 4
# Depth : 34
