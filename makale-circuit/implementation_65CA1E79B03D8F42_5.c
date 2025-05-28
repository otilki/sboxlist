// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[0];
F[3] = X[2];

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 11ee  BS[3] 3333 , Prev_Value 00ff , Rem Cost 700

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 44bb  BS[2] 11ee  BS[3] 3333 , Prev_Value 5555 , Rem Cost 900

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 11ee  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 1100

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 2dd2  BS[3] 3333 , Prev_Value 11ee , Rem Cost 1300

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 2dd2  BS[3] 7788 , Prev_Value 3333 , Rem Cost 1500

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 695a  BS[3] 7788 , Prev_Value 2dd2 , Rem Cost 2200

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 44bb  BS[2] 695a  BS[3] 7788 , Prev_Value 70b3 , Rem Cost 1900 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 70b3  BS[2] 695a  BS[3] 7788 , Prev_Value 4bb4 , Rem Cost 1200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 70b3  BS[2] 695a  BS[3] 7788 , Prev_Value 96a5 , Rem Cost 1000 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 70b3  BS[2] 96a5  BS[3] 7788 , Prev_Value e616 , Rem Cost 900 R

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] e616  BS[2] 96a5  BS[3] 7788 , Prev_Value 359c , Rem Cost 700 R


X[0] = F[3];
X[1] = F[1];
X[2] = F[2];
X[3] = F[0];

// to : 359C E616 96A5 4BB4 
// T-Depth : 4
// Depth : 34
