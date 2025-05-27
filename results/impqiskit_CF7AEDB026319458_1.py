# from : 00FF 0F0F 3333 5555 
#F[0] = X[2];
#F[1] = X[3];
#F[2] = X[0];
#F[3] = X[1];

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
circuit = QuantumCircuit(4)

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 00ff  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 100

circuit.x(2)
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] ff00  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 200

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] ff00  BS[3] a5f0 , Prev_Value f0f0 , Rem Cost 900

circuit.cx((1),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] aa55  BS[3] a5f0 , Prev_Value ff00 , Rem Cost 1100

circuit.ccx((3),(0),(2))
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 8b65  BS[3] a5f0 , Prev_Value aa55 , Rem Cost 1800

#circuit.cccx((0),(2),(3),(1))
#Qiskit doesn't natively support CCCX gates.
Info_Op:  , Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5475  BS[2] 8b65  BS[3] a5f0 , Prev_Value 5555 , Rem Cost 3900

circuit.ccx((2),(1),(0))
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 5475  BS[2] 8b65  BS[3] a5f0 , Prev_Value 3356 , Rem Cost 2500 R

circuit.cx((2),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3356  BS[1] 5475  BS[2] 8b65  BS[3] a5f0 , Prev_Value b833 , Rem Cost 1800 R

circuit.cx((1),(3))
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] b833  BS[1] 5475  BS[2] 8b65  BS[3] a5f0 , Prev_Value f185 , Rem Cost 1600 R

circuit.cx((0),(1))
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] b833  BS[1] 5475  BS[2] 8b65  BS[3] f185 , Prev_Value ec46 , Rem Cost 1400 R

circuit.cx((3),(2))
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] b833  BS[1] ec46  BS[2] 8b65  BS[3] f185 , Prev_Value 7ae0 , Rem Cost 1200 R

circuit.ccx((2),(1),(3))
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] b833  BS[1] ec46  BS[2] 7ae0  BS[3] f185 , Prev_Value 99c5 , Rem Cost 1000 R

circuit.x(3)
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] b833  BS[1] ec46  BS[2] 7ae0  BS[3] 99c5 , Prev_Value 663a , Rem Cost 300 R

circuit.cx((3),(0))
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] b833  BS[1] ec46  BS[2] 7ae0  BS[3] 663a , Prev_Value de09 , Rem Cost 200 R

print(circuit.depth()) #note that this is the non-decomposed depth
circuit.draw(output="mpl")
plt.show()
#X[0] = F[0];
#X[1] = F[1];
#X[2] = F[2];
#X[3] = F[3];

# to : DE09 EC46 7AE0 663A 
# T-Depth : 7
# Depth : 59
