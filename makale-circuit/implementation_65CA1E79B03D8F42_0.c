// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[0];
F[3] = X[2];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 00ff  BS[3] cccc , Prev_Value 3333 , Rem Cost 100

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 44bb  BS[3] cccc , Prev_Value 00ff , Rem Cost 800

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 4bb4  BS[1] 5555  BS[2] 44bb  BS[3] cccc , Prev_Value 0f0f , Rem Cost 1000

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 5555  BS[2] bb44  BS[3] cccc , Prev_Value 44bb , Rem Cost 1100

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 5555  BS[2] 7788  BS[3] cccc , Prev_Value bb44 , Rem Cost 1300

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 5555  BS[2] 7788  BS[3] 8f4c , Prev_Value cccc , Rem Cost 2000

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 5555  BS[2] 7788  BS[3] 8f4c , Prev_Value 525d , Rem Cost 1900 R

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 525d  BS[2] 7788  BS[3] 8f4c , Prev_Value 359c , Rem Cost 1200 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 525d  BS[2] 359c  BS[3] 8f4c , Prev_Value 19e9 , Rem Cost 500 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 19e9  BS[2] 359c  BS[3] 8f4c , Prev_Value 96a5 , Rem Cost 300 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 19e9  BS[2] 359c  BS[3] 96a5 , Prev_Value e616 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[1];
X[2] = F[3];
X[3] = F[0];

// to : 359C E616 96A5 4BB4 
// T-Depth : 4
// Depth : 39
