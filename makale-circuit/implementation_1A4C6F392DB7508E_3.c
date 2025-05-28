// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 3636 , Prev_Value 3333 , Rem Cost 700

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aaaa  BS[3] 3636 , Prev_Value 5555 , Rem Cost 800

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aa9c  BS[3] 3636 , Prev_Value aaaa , Rem Cost 1500

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aa9c  BS[3] c9c9 , Prev_Value 3636 , Rem Cost 1600

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aa9c  BS[3] c9c9 , Prev_Value 8787 , Rem Cost 2000 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 8787  BS[2] aa9c  BS[3] c9c9 , Prev_Value 8778 , Rem Cost 1300 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 8778  BS[1] 8787  BS[2] aa9c  BS[3] c9c9 , Prev_Value 4eb1 , Rem Cost 1100 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 8778  BS[1] 8787  BS[2] aa9c  BS[3] 4eb1 , Prev_Value 7878 , Rem Cost 900 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 8778  BS[1] 7878  BS[2] aa9c  BS[3] 4eb1 , Prev_Value 5563 , Rem Cost 800 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 8778  BS[1] 7878  BS[2] 5563  BS[3] 4eb1 , Prev_Value 3c59 , Rem Cost 700 R


X[0] = F[2];
X[1] = F[1];
X[2] = F[3];
X[3] = F[0];

// to : 5563 3C59 4EB1 8778 
// T-Depth : 4
// Depth : 34
