# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[0];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] f0f0  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 100

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] f0f0  BS[3] 6666 , Prev_Value 3333 , Rem Cost 300

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 55a5  BS[1] 00ff  BS[2] f0f0  BS[3] 6666 , Prev_Value 5555 , Rem Cost 1000

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55a5  BS[1] 00ff  BS[2] a555  BS[3] 6666 , Prev_Value f0f0 , Rem Cost 1200

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 55a5  BS[1] 555a  BS[2] a555  BS[3] 6666 , Prev_Value 00ff , Rem Cost 1400

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 55a5  BS[1] 555a  BS[2] a555  BS[3] c333 , Prev_Value 6666 , Rem Cost 1600

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 14b7  BS[1] 555a  BS[2] a555  BS[3] c333 , Prev_Value 55a5 , Rem Cost 2300

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 14b7  BS[1] 555a  BS[2] a555  BS[3] c333 , Prev_Value c726 , Rem Cost 1800 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 14b7  BS[1] 555a  BS[2] a555  BS[3] c726 , Prev_Value d05e , Rem Cost 1100 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 14b7  BS[1] d05e  BS[2] a555  BS[3] c726 , Prev_Value eb48 , Rem Cost 400 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] eb48  BS[1] d05e  BS[2] a555  BS[3] c726 , Prev_Value 38d9 , Rem Cost 300 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] eb48  BS[1] d05e  BS[2] a555  BS[3] 38d9 , Prev_Value 2fa1 , Rem Cost 200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] eb48  BS[1] 2fa1  BS[2] a555  BS[3] 38d9 , Prev_Value 5aaa , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[0];
#X[3] = F[2];

# to : 38D9 2FA1 EB48 5AAA 
# T-Depth : 4
# Depth : 35
