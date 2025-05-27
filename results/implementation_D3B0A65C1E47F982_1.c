// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[1];
F[3] = X[2];

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 0f0f  BS[3] 6666 , Prev_Value 3333 , Rem Cost 200

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 0ff0  BS[3] 6666 , Prev_Value 0f0f , Rem Cost 400

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 4bb4  BS[3] 6666 , Prev_Value 0ff0 , Rem Cost 1100

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 1ee1  BS[2] 4bb4  BS[3] 6666 , Prev_Value 5555 , Rem Cost 1300

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value 4bb4 , Rem Cost 2000

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value 0a3f , Rem Cost 2100 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0a3f  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value 6c59 , Rem Cost 1400 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 6c59  BS[1] 1ee1  BS[2] 4bd2  BS[3] 6666 , Prev_Value e11e , Rem Cost 1200 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 6c59  BS[1] e11e  BS[2] 4bd2  BS[3] 6666 , Prev_Value 8778 , Rem Cost 1100 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 6c59  BS[1] e11e  BS[2] 4bd2  BS[3] 8778 , Prev_Value a94e , Rem Cost 900 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6c59  BS[1] a94e  BS[2] 4bd2  BS[3] 8778 , Prev_Value e29c , Rem Cost 200 R


X[0] = F[1];
X[1] = F[3];
X[2] = F[0];
X[3] = F[2];

// to : A94E 8778 6C59 E29C 
// T-Depth : 4
// Depth : 38
