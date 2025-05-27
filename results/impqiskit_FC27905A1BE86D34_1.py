# from : 00FF 0F0F 3333 5555 
#F[0] = X[1];
#F[1] = X[3];
#F[2] = X[2];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 3333  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 6666  BS[2] 3333  BS[3] ff00 , Prev_Value 5555 , Rem Cost 300

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2d2d  BS[1] 6666  BS[2] 3333  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 1000

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 2d2d  BS[1] 6666  BS[2] 5533  BS[3] ff00 , Prev_Value 3333 , Rem Cost 1700

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 2d2d  BS[1] 9999  BS[2] 5533  BS[3] ff00 , Prev_Value 6666 , Rem Cost 1800

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 2d2d  BS[1] 9999  BS[2] aacc  BS[3] ff00 , Prev_Value 5533 , Rem Cost 1900

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 2d2d  BS[1] 9999  BS[2] aacc  BS[3] ff00 , Prev_Value b195 , Rem Cost 2400 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2d2d  BS[1] b195  BS[2] aacc  BS[3] ff00 , Prev_Value 87e1 , Rem Cost 1700 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2d2d  BS[1] b195  BS[2] 87e1  BS[3] ff00 , Prev_Value 4e95 , Rem Cost 1500 R

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2d2d  BS[1] 4e95  BS[2] 87e1  BS[3] ff00 , Prev_Value d22d , Rem Cost 1300 R

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2d2d  BS[1] 4e95  BS[2] 87e1  BS[3] d22d , Prev_Value c974 , Rem Cost 1100 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2d2d  BS[1] 4e95  BS[2] c974  BS[3] d22d , Prev_Value 6539 , Rem Cost 900 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 6539  BS[1] 4e95  BS[2] c974  BS[3] d22d , Prev_Value 9ac6 , Rem Cost 200 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 9ac6  BS[1] 4e95  BS[2] c974  BS[3] d22d , Prev_Value b16a , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[3];
#X[2] = F[1];
#X[3] = F[0];

# to : C974 D22D B16A 9AC6 
# T-Depth : 4
# Depth : 36
