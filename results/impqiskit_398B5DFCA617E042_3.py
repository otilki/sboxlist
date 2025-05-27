# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 0f5a  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 0f5a  BS[3] ff00 , Prev_Value 00ff , Rem Cost 800

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5647  BS[2] 0f5a  BS[3] ff00 , Prev_Value 5555 , Rem Cost 1500

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5647  BS[2] f0a5  BS[3] ff00 , Prev_Value 0f5a , Rem Cost 1600

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5647  BS[2] f0a5  BS[3] ff00 , Prev_Value ed03 , Rem Cost 2100 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 5647  BS[2] f0a5  BS[3] ed03 , Prev_Value de30 , Rem Cost 1400 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] de30  BS[1] 5647  BS[2] f0a5  BS[3] ed03 , Prev_Value 8877 , Rem Cost 1200 R

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] de30  BS[1] 8877  BS[2] f0a5  BS[3] ed03 , Prev_Value 6d26 , Rem Cost 1000 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] de30  BS[1] 8877  BS[2] f0a5  BS[3] 6d26 , Prev_Value 7788 , Rem Cost 300 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] de30  BS[1] 7788  BS[2] f0a5  BS[3] 6d26 , Prev_Value 0f5a , Rem Cost 200 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] de30  BS[1] 7788  BS[2] 0f5a  BS[3] 6d26 , Prev_Value 92d9 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[1];
#X[1] = F[2];
#X[2] = F[3];
#X[3] = F[0];

# to : 7788 0F5A 92D9 DE30 
# T-Depth : 4
# Depth : 33
