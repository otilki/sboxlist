# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[0];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] 5555 , Prev_Value 00ff , Rem Cost 200

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] aaaa , Prev_Value 5555 , Rem Cost 300

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] a9a9 , Prev_Value aaaa , Rem Cost 1000

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 9a9a  BS[2] 55aa  BS[3] a9a9 , Prev_Value 3333 , Rem Cost 1200

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 5aa5  BS[1] 9a9a  BS[2] 55aa  BS[3] a9a9 , Prev_Value 0f0f , Rem Cost 1400

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5aa5  BS[1] 9a9a  BS[2] 55aa  BS[3] f30c , Prev_Value a9a9 , Rem Cost 1600

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5aa5  BS[1] 9a9a  BS[2] cf30  BS[3] f30c , Prev_Value 55aa , Rem Cost 1800

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 5aa5  BS[1] 9a9a  BS[2] d5b0  BS[3] f30c , Prev_Value cf30 , Rem Cost 2500

#circuit.cccx((1),(2),(3),(0))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 5aa5  BS[1] 9a9a  BS[2] d5b0  BS[3] f30c , Prev_Value caa5 , Rem Cost 3900 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] caa5  BS[1] 9a9a  BS[2] d5b0  BS[3] f30c , Prev_Value 4b9a , Rem Cost 1800 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] caa5  BS[1] 4b9a  BS[2] d5b0  BS[3] f30c , Prev_Value 813f , Rem Cost 1100 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] caa5  BS[1] 813f  BS[2] d5b0  BS[3] f30c , Prev_Value 7329 , Rem Cost 900 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] caa5  BS[1] 813f  BS[2] d5b0  BS[3] 7329 , Prev_Value 7ec0 , Rem Cost 200 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] caa5  BS[1] 7ec0  BS[2] d5b0  BS[3] 7329 , Prev_Value 8cd6 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[0];

# to : 7EC0 8CD6 D5B0 CAA5 
# T-Depth : 7
# Depth : 59
