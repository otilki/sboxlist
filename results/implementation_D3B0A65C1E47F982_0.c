// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[1];
F[3] = X[2];

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 200

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 8787  BS[3] cccc , Prev_Value 0f0f , Rem Cost 900

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aa55  BS[2] 8787  BS[3] cccc , Prev_Value aaaa , Rem Cost 1100

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6699  BS[2] 8787  BS[3] cccc , Prev_Value aa55 , Rem Cost 1300

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 6699  BS[2] 8787  BS[3] cc55 , Prev_Value cccc , Rem Cost 2000

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6699  BS[2] 8787  BS[3] cc55 , Prev_Value e29c , Rem Cost 2000 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] e29c  BS[2] 8787  BS[3] cc55 , Prev_Value 8778 , Rem Cost 1300 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 8778  BS[1] e29c  BS[2] 8787  BS[3] cc55 , Prev_Value 651b , Rem Cost 1100 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 8778  BS[1] e29c  BS[2] 651b  BS[3] cc55 , Prev_Value a94e , Rem Cost 900 R

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 8778  BS[1] e29c  BS[2] a94e  BS[3] cc55 , Prev_Value 6c59 , Rem Cost 700 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : A94E 8778 6C59 E29C 
// T-Depth : 4
// Depth : 39
