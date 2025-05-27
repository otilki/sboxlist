# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[3];
#F[2] = X[1];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3c3c  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 300

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3c3c  BS[3] 1b1b , Prev_Value 3333 , Rem Cost 1000

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] c3c3  BS[3] 1b1b , Prev_Value 3c3c , Rem Cost 1100

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] c3d8  BS[3] 1b1b , Prev_Value c3c3 , Rem Cost 1800

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] c3d8  BS[3] d8c3 , Prev_Value 1b1b , Rem Cost 2000

circuit.ccx((3),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 887d  BS[1] aaaa  BS[2] c3d8  BS[3] d8c3 , Prev_Value 00ff , Rem Cost 2700

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 887d  BS[1] aaaa  BS[2] c3d8  BS[3] d8c3 , Prev_Value 2af2 , Rem Cost 2500 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 887d  BS[1] 2af2  BS[2] c3d8  BS[3] d8c3 , Prev_Value a28f , Rem Cost 1800 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 887d  BS[1] a28f  BS[2] c3d8  BS[3] d8c3 , Prev_Value 50be , Rem Cost 1600 R

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 50be  BS[1] a28f  BS[2] c3d8  BS[3] d8c3 , Prev_Value c356 , Rem Cost 1400 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 50be  BS[1] a28f  BS[2] c356  BS[3] d8c3 , Prev_Value 61d9 , Rem Cost 700 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 50be  BS[1] 61d9  BS[2] c356  BS[3] d8c3 , Prev_Value 273c , Rem Cost 500 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 50be  BS[1] 61d9  BS[2] c356  BS[3] 273c , Prev_Value 7782 , Rem Cost 400 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 7782  BS[1] 61d9  BS[2] c356  BS[3] 273c , Prev_Value b4d4 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[2];
#X[2] = F[1];
#X[3] = F[3];

# to : 7782 B4D4 61D9 273C 
# T-Depth : 5
# Depth : 48
