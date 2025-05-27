# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 200

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 900

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0f0 , Prev_Value aaaa , Rem Cost 1100

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value f0f0 , Rem Cost 1800

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value 12fc , Rem Cost 1800 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value 21cf , Rem Cost 1100 R

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 12fc  BS[1] 21cf  BS[2] 8877  BS[3] f0a5 , Prev_Value 92d9 , Rem Cost 900 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 92d9  BS[1] 21cf  BS[2] 8877  BS[3] f0a5 , Prev_Value 6d26 , Rem Cost 200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 6d26  BS[1] 21cf  BS[2] 8877  BS[3] f0a5 , Prev_Value 7788 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[0];
#X[3] = F[1];

# to : 7788 F0A5 6D26 21CF 
# T-Depth : 4
# Depth : 34
