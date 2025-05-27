# from : 00FF 0F0F 3333 5555 
#F[0] = X[3];
#F[1] = X[2];
#F[2] = X[1];
#F[3] = X[0];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 0ff0  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 200

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 0ff0  BS[3] 55aa , Prev_Value 00ff , Rem Cost 400

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 3333  BS[2] 0ff0  BS[3] 55aa , Prev_Value 5555 , Rem Cost 500

circuit.cx((2),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] 3cc3  BS[2] 0ff0  BS[3] 55aa , Prev_Value 3333 , Rem Cost 700

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] 3cc3  BS[2] f00f  BS[3] 55aa , Prev_Value 0ff0 , Rem Cost 800

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] 3cc3  BS[2] e48d  BS[3] 55aa , Prev_Value f00f , Rem Cost 1500

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] 3cc3  BS[2] e48d  BS[3] ff00 , Prev_Value 55aa , Rem Cost 1700

circuit.ccx((3),(2),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] d8c3  BS[2] e48d  BS[3] ff00 , Prev_Value 3cc3 , Rem Cost 2400

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] d8c3  BS[2] e48d  BS[3] ff00 , Prev_Value 7782 , Rem Cost 2700 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] d8c3  BS[2] e48d  BS[3] 7782 , Prev_Value 4e27 , Rem Cost 2000 R

circuit.x(1)
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 4e27  BS[1] d8c3  BS[2] e48d  BS[3] 7782 , Prev_Value 273c , Rem Cost 1800 R

circuit.x(0)
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 4e27  BS[1] 273c  BS[2] e48d  BS[3] 7782 , Prev_Value b1d8 , Rem Cost 1700 R

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] b1d8  BS[1] 273c  BS[2] e48d  BS[3] 7782 , Prev_Value d50d , Rem Cost 1600 R

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] b1d8  BS[1] 273c  BS[2] d50d  BS[3] 7782 , Prev_Value b4d4 , Rem Cost 900 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] b4d4  BS[1] 273c  BS[2] d50d  BS[3] 7782 , Prev_Value 61d9 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[3];
#X[1] = F[0];
#X[2] = F[2];
#X[3] = F[1];

# to : 7782 B4D4 61D9 273C 
# T-Depth : 5
# Depth : 47
