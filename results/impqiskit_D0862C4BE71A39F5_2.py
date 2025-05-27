# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 0f3c  BS[2] 5555  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 700

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 0f3c  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 800

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] f0c3  BS[2] 5555  BS[3] ff00 , Prev_Value 0f3c , Rem Cost 900

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 6666  BS[1] f0c3  BS[2] 5555  BS[3] ff00 , Prev_Value 3333 , Rem Cost 1100

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6666  BS[1] f0c3  BS[2] a596  BS[3] ff00 , Prev_Value 5555 , Rem Cost 1300

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 6666  BS[1] 96c3  BS[2] a596  BS[3] ff00 , Prev_Value f0c3 , Rem Cost 2000

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 6666  BS[1] 96c3  BS[2] a596  BS[3] ff00 , Prev_Value 9999 , Rem Cost 1600 R

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 9999  BS[1] 96c3  BS[2] a596  BS[3] ff00 , Prev_Value 7e90 , Rem Cost 1500 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 9999  BS[1] 96c3  BS[2] a596  BS[3] 7e90 , Prev_Value 816f , Rem Cost 800 R

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 9999  BS[1] 96c3  BS[2] a596  BS[3] 816f , Prev_Value 19da , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[0];
#X[3] = F[3];

# to : A596 96C3 19DA 816F 
# T-Depth : 4
# Depth : 34
