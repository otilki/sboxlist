# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[1];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 333c  BS[1] 00ff  BS[2] 0f0f  BS[3] 5555 , Prev_Value 3333 , Rem Cost 700

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 333c  BS[1] 00ff  BS[2] 3c33  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 900

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 33c3  BS[2] 3c33  BS[3] 5555 , Prev_Value 00ff , Rem Cost 1100

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 227d  BS[1] 33c3  BS[2] 3c33  BS[3] 5555 , Prev_Value 333c , Rem Cost 1800

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 227d  BS[1] 33c3  BS[2] 3c33  BS[3] 6966 , Prev_Value 5555 , Rem Cost 2000

#circuit.cccx((0),(1),(2),(3))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 3, Op_Values  BS[0] 227d  BS[1] 33c3  BS[2] 3c33  BS[3] 4967 , Prev_Value 6966 , Rem Cost 4100

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 227d  BS[1] 33c3  BS[2] 3c33  BS[3] 4967 , Prev_Value 33a6 , Rem Cost 2400 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 227d  BS[1] 33a6  BS[2] 3c33  BS[3] 4967 , Prev_Value 1e4e , Rem Cost 1700 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1e4e  BS[1] 33a6  BS[2] 3c33  BS[3] 4967 , Prev_Value 2e35 , Rem Cost 1500 R

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1e4e  BS[1] 33a6  BS[2] 2e35  BS[3] 4967 , Prev_Value 6752 , Rem Cost 800 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1e4e  BS[1] 33a6  BS[2] 2e35  BS[3] 6752 , Prev_Value 791c , Rem Cost 600 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 791c  BS[1] 33a6  BS[2] 2e35  BS[3] 6752 , Prev_Value 86e3 , Rem Cost 400 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 86e3  BS[1] 33a6  BS[2] 2e35  BS[3] 6752 , Prev_Value d1ca , Rem Cost 300 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 86e3  BS[1] 33a6  BS[2] d1ca  BS[3] 6752 , Prev_Value e26c , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[0];

# to : 6752 E26C D1CA 86E3 
# T-Depth : 7
# Depth : 62
