# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] cccc  BS[3] 00ff , Prev_Value 3333 , Rem Cost 100

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] cccc  BS[3] 05fa , Prev_Value 00ff , Rem Cost 800

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 50af  BS[2] cccc  BS[3] 05fa , Prev_Value 5555 , Rem Cost 1000

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 50af  BS[2] cccc  BS[3] fa05 , Prev_Value 05fa , Rem Cost 1100

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 98ab  BS[2] cccc  BS[3] fa05 , Prev_Value 50af , Rem Cost 1800

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 98ab  BS[2] cccc  BS[3] fa05 , Prev_Value 8787 , Rem Cost 1900 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 8787  BS[1] 98ab  BS[2] cccc  BS[3] fa05 , Prev_Value 4ec9 , Rem Cost 1200 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 8787  BS[1] 98ab  BS[2] 4ec9  BS[3] fa05 , Prev_Value d662 , Rem Cost 500 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 8787  BS[1] 98ab  BS[2] d662  BS[3] fa05 , Prev_Value 1f2c , Rem Cost 300 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 8787  BS[1] 1f2c  BS[2] d662  BS[3] fa05 , Prev_Value 7878 , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[3];
#X[2] = F[2];
#X[3] = F[1];

# to : 7878 FA05 D662 1F2C 
# T-Depth : 4
# Depth : 36
