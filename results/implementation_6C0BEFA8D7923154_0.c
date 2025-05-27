// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[1];
F[3] = X[2];

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 0f0f  BS[3] 333c , Prev_Value 3333 , Rem Cost 700

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 3c33  BS[3] 333c , Prev_Value 0f0f , Rem Cost 900

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 3c33  BS[3] ccc3 , Prev_Value 333c , Rem Cost 1000

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3c33  BS[3] ccc3 , Prev_Value 5555 , Rem Cost 1100

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] b4b1  BS[3] ccc3 , Prev_Value 3c33 , Rem Cost 1800

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] b4b1  BS[3] ccc3 , Prev_Value a05f , Rem Cost 1900 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] a05f  BS[1] aaaa  BS[2] b4b1  BS[3] ccc3 , Prev_Value 2ae9 , Rem Cost 1200 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] a05f  BS[1] 2ae9  BS[2] b4b1  BS[3] ccc3 , Prev_Value 9e58 , Rem Cost 500 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] a05f  BS[1] 9e58  BS[2] b4b1  BS[3] ccc3 , Prev_Value 14ee , Rem Cost 300 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] a05f  BS[1] 9e58  BS[2] 14ee  BS[3] ccc3 , Prev_Value 5fa0 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[1];
X[3] = F[2];

// to : 5FA0 CCC3 9E58 14EE 
// T-Depth : 4
// Depth : 36
