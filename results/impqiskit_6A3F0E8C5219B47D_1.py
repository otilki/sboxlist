# from : 00FF 0F0F 3333 5555 
#F[0] = X[0];
#F[1] = X[2];
#F[2] = X[3];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 33cc  BS[2] 5555  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 200

circuit.cx((0),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 33cc  BS[2] 5555  BS[3] 0ff0 , Prev_Value 0f0f , Rem Cost 400

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 33cc  BS[2] 6699  BS[3] 0ff0 , Prev_Value 5555 , Rem Cost 600

circuit.ccx((3),(2),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 066f  BS[1] 33cc  BS[2] 6699  BS[3] 0ff0 , Prev_Value 00ff , Rem Cost 1300

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 066f  BS[1] 33cc  BS[2] 6699  BS[3] f00f , Prev_Value 0ff0 , Rem Cost 1400

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 066f  BS[1] 33cc  BS[2] 5555  BS[3] f00f , Prev_Value 6699 , Rem Cost 1600

circuit.ccx((2),(0),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 066f  BS[1] 33cc  BS[2] 5555  BS[3] f44a , Prev_Value f00f , Rem Cost 2300

circuit.ccx((1),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 066f  BS[1] 33cc  BS[2] 5555  BS[3] f44a , Prev_Value 5719 , Rem Cost 2200 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 066f  BS[1] 33cc  BS[2] 5719  BS[3] f44a , Prev_Value f225 , Rem Cost 1500 R

circuit.ccx((2),(0),(1))
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] f225  BS[1] 33cc  BS[2] 5719  BS[3] f44a , Prev_Value 61cd , Rem Cost 1300 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] f225  BS[1] 61cd  BS[2] 5719  BS[3] f44a , Prev_Value a53c , Rem Cost 600 R

circuit.cx((3),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] a53c  BS[1] 61cd  BS[2] 5719  BS[3] f44a , Prev_Value 9587 , Rem Cost 400 R

circuit.cx((1),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] a53c  BS[1] 9587  BS[2] 5719  BS[3] f44a , Prev_Value 30bb , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[2];
#X[1] = F[1];
#X[2] = F[3];
#X[3] = F[0];

# to : 5719 9587 F44A 30BB 
# T-Depth : 4
# Depth : 40
