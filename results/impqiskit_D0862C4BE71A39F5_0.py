# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[0];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] aaaa  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] aaaa  BS[3] a5a5 , Prev_Value 0f0f , Rem Cost 300

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 9999  BS[3] a5a5 , Prev_Value aaaa , Rem Cost 500

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 9999  BS[3] a596 , Prev_Value a5a5 , Rem Cost 1200

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value 00ff , Rem Cost 1900

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value b23a , Rem Cost 1800 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] b23a  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value 17ac , Rem Cost 1100 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 17ac  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value 96c3 , Rem Cost 900 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 96c3  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value 19da , Rem Cost 700 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[2];
#X[3] = F[1];

# to : A596 96C3 19DA 816F 
# T-Depth : 4
# Depth : 37
