# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 5555  BS[3] 05fa , Prev_Value 00ff , Rem Cost 700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] aaaa  BS[3] 05fa , Prev_Value 5555 , Rem Cost 800

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] aaaa  BS[3] fa05 , Prev_Value 05fa , Rem Cost 900

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 98ab  BS[3] fa05 , Prev_Value aaaa , Rem Cost 1600

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 98ab  BS[3] fa05 , Prev_Value 1f2c , Rem Cost 2000 R

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 1f2c  BS[1] 3333  BS[2] 98ab  BS[3] fa05 , Prev_Value ab98 , Rem Cost 1300 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 1f2c  BS[1] ab98  BS[2] 98ab  BS[3] fa05 , Prev_Value 8787 , Rem Cost 1100 R

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1f2c  BS[1] ab98  BS[2] 8787  BS[3] fa05 , Prev_Value 299d , Rem Cost 900 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1f2c  BS[1] 299d  BS[2] 8787  BS[3] fa05 , Prev_Value 7878 , Rem Cost 200 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 1f2c  BS[1] 299d  BS[2] 7878  BS[3] fa05 , Prev_Value d662 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : 7878 FA05 D662 1F2C 
# T-Depth : 4
# Depth : 34
