# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[2];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3333  BS[3] 5656 , Prev_Value 5555 , Rem Cost 700

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3c3c  BS[3] 5656 , Prev_Value 3333 , Rem Cost 900

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3cc3  BS[3] 5656 , Prev_Value 3c3c , Rem Cost 1100

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 1b4d  BS[2] 3cc3  BS[3] 5656 , Prev_Value 0f0f , Rem Cost 1800

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 1b4d  BS[2] 3c8e  BS[3] 5656 , Prev_Value 3cc3 , Rem Cost 2500

#circuit.cccx((1),(2),(3),(0))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 1b4d  BS[2] 3c8e  BS[3] 5656 , Prev_Value 10fb , Rem Cost 3700 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 10fb  BS[1] 1b4d  BS[2] 3c8e  BS[3] 5656 , Prev_Value 2c75 , Rem Cost 1600 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 10fb  BS[1] 1b4d  BS[2] 2c75  BS[3] 5656 , Prev_Value 46ad , Rem Cost 1400 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 46ad  BS[1] 1b4d  BS[2] 2c75  BS[3] 5656 , Prev_Value 3738 , Rem Cost 1200 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 46ad  BS[1] 3738  BS[2] 2c75  BS[3] 5656 , Prev_Value c8c7 , Rem Cost 1000 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 46ad  BS[1] c8c7  BS[2] 2c75  BS[3] 5656 , Prev_Value 9e91 , Rem Cost 900 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 46ad  BS[1] c8c7  BS[2] 2c75  BS[3] 9e91 , Prev_Value cce2 , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[2];

# to : 46AD 9E91 CCE2 2C75 
# T-Depth : 7
# Depth : 60
