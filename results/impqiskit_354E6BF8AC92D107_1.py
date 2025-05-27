# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[1];
#F[2] = X[3];
#F[3] = X[2];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 3c3c , Prev_Value 3333 , Rem Cost 200

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 0f0f  BS[2] 5555  BS[3] 3c3c , Prev_Value 00ff , Rem Cost 400

circuit.ccx((3),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 55aa  BS[1] 1b27  BS[2] 5555  BS[3] 3c3c , Prev_Value 0f0f , Rem Cost 1100

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55aa  BS[1] 1b27  BS[2] 4e72  BS[3] 3c3c , Prev_Value 5555 , Rem Cost 1300

circuit.cx((2),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 1b27  BS[2] 4e72  BS[3] 724e , Prev_Value 3c3c , Rem Cost 1500

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 4e72  BS[3] 724e , Prev_Value 55aa , Rem Cost 2200

circuit.ccx((1),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 4e72  BS[3] 724e , Prev_Value 616e , Rem Cost 2000 R

circuit.cx((0),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 4e72  BS[3] 616e , Prev_Value 599a , Rem Cost 1300 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 599a  BS[3] 616e , Prev_Value 7a49 , Rem Cost 1100 R

circuit.ccx((3),(1),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 7a49  BS[2] 599a  BS[3] 616e , Prev_Value 39d2 , Rem Cost 900 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 17e8  BS[1] 7a49  BS[2] 39d2  BS[3] 616e , Prev_Value 9e91 , Rem Cost 200 R

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 7a49  BS[2] 39d2  BS[3] 9e91 , Prev_Value c62d , Rem Cost 100 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[2];

# to : 17E8 7A49 9E91 C62D 
# T-Depth : 4
# Depth : 37
