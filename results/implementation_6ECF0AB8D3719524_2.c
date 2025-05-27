// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[3];
F[3] = X[1];

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 5555  BS[3] 0f5a , Prev_Value 0f0f , Rem Cost 700

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] 0f5a , Prev_Value 5555 , Rem Cost 800

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] f0a5 , Prev_Value 0f5a , Rem Cost 900

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 9a8b  BS[3] f0a5 , Prev_Value aaaa , Rem Cost 1600

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 9a8b  BS[3] f0a5 , Prev_Value 12fc , Rem Cost 2000 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] 3333  BS[2] 9a8b  BS[3] f0a5 , Prev_Value a9b8 , Rem Cost 1300 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 12fc  BS[1] a9b8  BS[2] 9a8b  BS[3] f0a5 , Prev_Value 8877 , Rem Cost 1100 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] a9b8  BS[2] 8877  BS[3] f0a5 , Prev_Value 299d , Rem Cost 900 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 12fc  BS[1] 299d  BS[2] 8877  BS[3] f0a5 , Prev_Value 7788 , Rem Cost 200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] 299d  BS[2] 7788  BS[3] f0a5 , Prev_Value d662 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[1];
X[3] = F[0];

// to : 7788 F0A5 D662 12FC 
// T-Depth : 4
// Depth : 34
