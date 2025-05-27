# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[1];
#F[3] = X[3];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 0f0f  BS[3] 55aa , Prev_Value 5555 , Rem Cost 200

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 0f0f  BS[3] 6699 , Prev_Value 55aa , Rem Cost 400

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 6996  BS[3] 6699 , Prev_Value 0f0f , Rem Cost 600

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 6996  BS[3] 9966 , Prev_Value 6699 , Rem Cost 700

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3355  BS[1] 00ff  BS[2] 6996  BS[3] 9966 , Prev_Value 3333 , Rem Cost 1400

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3355  BS[1] 00ff  BS[2] 6996  BS[3] aa33 , Prev_Value 9966 , Rem Cost 1600

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3355  BS[1] 6969  BS[2] 6996  BS[3] aa33 , Prev_Value 00ff , Rem Cost 1800

#circuit.cccx((1),(2),(3),(0))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 1b55  BS[1] 6969  BS[2] 6996  BS[3] aa33 , Prev_Value 3355 , Rem Cost 3900

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1b55  BS[1] 6969  BS[2] 6996  BS[3] aa33 , Prev_Value 6378 , Rem Cost 2600 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1b55  BS[1] 6378  BS[2] 6996  BS[3] aa33 , Prev_Value 6ac6 , Rem Cost 1900 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 1b55  BS[1] 6378  BS[2] 6ac6  BS[3] aa33 , Prev_Value 7915 , Rem Cost 1200 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 7915  BS[1] 6378  BS[2] 6ac6  BS[3] aa33 , Prev_Value d326 , Rem Cost 500 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 7915  BS[1] 6378  BS[2] 6ac6  BS[3] d326 , Prev_Value 1a6d , Rem Cost 300 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 1a6d  BS[1] 6378  BS[2] 6ac6  BS[3] d326 , Prev_Value 2cd9 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[1];

# to : 1A6D 2CD9 6AC6 6378 
# T-Depth : 7
# Depth : 62
