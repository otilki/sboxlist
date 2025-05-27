# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[0];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5555  BS[3] 3333 , Prev_Value 00ff , Rem Cost 200

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5555  BS[3] 2277 , Prev_Value 3333 , Rem Cost 900

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] cc33  BS[2] 5555  BS[3] 2277 , Prev_Value 33cc , Rem Cost 1000

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] cc33  BS[2] aaaa  BS[3] 2277 , Prev_Value 5555 , Rem Cost 1100

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2d78  BS[1] cc33  BS[2] aaaa  BS[3] 2277 , Prev_Value 0f0f , Rem Cost 1300

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2d78  BS[1] cc33  BS[2] aaaa  BS[3] ee44 , Prev_Value 2277 , Rem Cost 1500

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2d78  BS[1] cc33  BS[2] 87d2  BS[3] ee44 , Prev_Value aaaa , Rem Cost 1700

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2d78  BS[1] 4be1  BS[2] 87d2  BS[3] ee44 , Prev_Value cc33 , Rem Cost 1900

#circuit.cccx((0),(2),(3),(1))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 1, Op_Values  BS[0] 2d78  BS[1] 4fa1  BS[2] 87d2  BS[3] ee44 , Prev_Value 4be1 , Rem Cost 4000

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2d78  BS[1] 4fa1  BS[2] 87d2  BS[3] ee44 , Prev_Value 6378 , Rem Cost 2600 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] 87d2  BS[3] ee44 , Prev_Value ed14 , Rem Cost 1900 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] 87d2  BS[3] ed14 , Prev_Value 6ac6 , Rem Cost 1200 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] 87d2  BS[3] 6ac6 , Prev_Value e592 , Rem Cost 1000 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] e592  BS[3] 6ac6 , Prev_Value 2cd9 , Rem Cost 300 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 6378  BS[1] 2cd9  BS[2] e592  BS[3] 6ac6 , Prev_Value 1a6d , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[0];

# to : 1A6D 2CD9 6AC6 6378 
# T-Depth : 7
# Depth : 61
