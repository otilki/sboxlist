# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 5555  BS[3] 0f5a , Prev_Value 0f0f , Rem Cost 700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] 0f5a , Prev_Value 5555 , Rem Cost 800

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] f0a5 , Prev_Value 0f5a , Rem Cost 900

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 9a8b  BS[3] f0a5 , Prev_Value aaaa , Rem Cost 1600

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 9a8b  BS[3] f0a5 , Prev_Value 12fc , Rem Cost 2000 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] 3333  BS[2] 9a8b  BS[3] f0a5 , Prev_Value a9b8 , Rem Cost 1300 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 12fc  BS[1] a9b8  BS[2] 9a8b  BS[3] f0a5 , Prev_Value 8877 , Rem Cost 1100 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] a9b8  BS[2] 8877  BS[3] f0a5 , Prev_Value 299d , Rem Cost 900 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 12fc  BS[1] 299d  BS[2] 8877  BS[3] f0a5 , Prev_Value 7788 , Rem Cost 200 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] 299d  BS[2] 7788  BS[3] f0a5 , Prev_Value d662 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : 7788 F0A5 D662 12FC 
# T-Depth : 4
# Depth : 34
