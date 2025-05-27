// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 3c3c , Prev_Value 3333 , Rem Cost 200

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 0f0f  BS[2] 5555  BS[3] 3c3c , Prev_Value 00ff , Rem Cost 400

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 55aa  BS[1] 1b27  BS[2] 5555  BS[3] 3c3c , Prev_Value 0f0f , Rem Cost 1100

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55aa  BS[1] 1b27  BS[2] 4e72  BS[3] 3c3c , Prev_Value 5555 , Rem Cost 1300

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 1b27  BS[2] 4e72  BS[3] 724e , Prev_Value 3c3c , Rem Cost 1500

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 4e72  BS[3] 724e , Prev_Value 55aa , Rem Cost 2200

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 4e72  BS[3] 724e , Prev_Value 616e , Rem Cost 2000 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 4e72  BS[3] 616e , Prev_Value 599a , Rem Cost 1300 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 17e8  BS[1] 1b27  BS[2] 599a  BS[3] 616e , Prev_Value 7a49 , Rem Cost 1100 R

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 7a49  BS[2] 599a  BS[3] 616e , Prev_Value 39d2 , Rem Cost 900 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 17e8  BS[1] 7a49  BS[2] 39d2  BS[3] 616e , Prev_Value 9e91 , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 7a49  BS[2] 39d2  BS[3] 9e91 , Prev_Value c62d , Rem Cost 100 R


X[0] = F[0];
X[1] = F[1];
X[2] = F[3];
X[3] = F[2];

// to : 17E8 7A49 9E91 C62D 
// T-Depth : 4
// Depth : 37
