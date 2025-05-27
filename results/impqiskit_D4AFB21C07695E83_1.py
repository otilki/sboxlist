# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[0];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 5555  BS[2] 00ff  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 200

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 5555  BS[2] 00ff  BS[3] 33cc , Prev_Value 3333 , Rem Cost 400

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 00ff  BS[3] 33cc , Prev_Value 5555 , Rem Cost 1100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 00ff  BS[3] cc33 , Prev_Value 33cc , Rem Cost 1200

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] ff00  BS[3] cc33 , Prev_Value 00ff , Rem Cost 1300

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 9a59  BS[3] cc33 , Prev_Value ff00 , Rem Cost 1500

#circuit.cccx((0),(1),(2),(3))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 9a59  BS[3] cc2b , Prev_Value cc33 , Rem Cost 3600

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 9a59  BS[3] cc2b , Prev_Value 3c65 , Rem Cost 2500 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] 6559  BS[2] 9a59  BS[3] cc2b , Prev_Value a972 , Rem Cost 1800 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] 6559  BS[2] 9a59  BS[3] a972 , Prev_Value ed09 , Rem Cost 1600 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] ed09  BS[2] 9a59  BS[3] a972 , Prev_Value d16c , Rem Cost 900 R

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] d16c  BS[2] 9a59  BS[3] a972 , Prev_Value b916 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[0];
#X[3] = F[2];

# to : B916 D16C 3C65 9A59 
# T-Depth : 7
# Depth : 59
