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

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] ff00  BS[1] cccc  BS[2] 5555  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 200

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] ff00  BS[1] cccc  BS[2] 5555  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 300

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] ff00  BS[1] cccc  BS[2] 9999  BS[3] f0f0 , Prev_Value 5555 , Rem Cost 500

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] ff00  BS[1] 3ccc  BS[2] 9999  BS[3] f0f0 , Prev_Value cccc , Rem Cost 1200

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 3ccc  BS[2] 9999  BS[3] f0f0 , Prev_Value ff00 , Rem Cost 1400

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0ff0  BS[1] 3ccc  BS[2] 9999  BS[3] fc30 , Prev_Value f0f0 , Rem Cost 2100

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 3ccc  BS[2] 9999  BS[3] fc30 , Prev_Value 1778 , Rem Cost 2100 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1778  BS[1] 3ccc  BS[2] 9999  BS[3] fc30 , Prev_Value eb48 , Rem Cost 1400 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 1778  BS[1] 3ccc  BS[2] 9999  BS[3] eb48 , Prev_Value a555 , Rem Cost 1200 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1778  BS[1] a555  BS[2] 9999  BS[3] eb48 , Prev_Value 38d9 , Rem Cost 1000 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1778  BS[1] a555  BS[2] 38d9  BS[3] eb48 , Prev_Value 2fa1 , Rem Cost 300 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 2fa1  BS[1] a555  BS[2] 38d9  BS[3] eb48 , Prev_Value 5aaa , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[0];
#X[2] = F[3];
#X[3] = F[1];

# to : 38D9 2FA1 EB48 5AAA 
# T-Depth : 4
# Depth : 37
