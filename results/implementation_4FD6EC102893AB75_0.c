// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[1];
F[3] = X[0];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] f0f0  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] f0f0  BS[3] ff00 , Prev_Value 00ff , Rem Cost 200

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 5555  BS[1] 6363  BS[2] f0f0  BS[3] ff00 , Prev_Value 3333 , Rem Cost 900

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 6363  BS[2] 9393  BS[3] ff00 , Prev_Value f0f0 , Rem Cost 1100

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 6363  BS[2] 9393  BS[3] fc03 , Prev_Value ff00 , Rem Cost 1800

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 5555  BS[1] 6363  BS[2] 9393  BS[3] fc03 , Prev_Value c556 , Rem Cost 1800 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] c556  BS[1] 6363  BS[2] 9393  BS[3] fc03 , Prev_Value a761 , Rem Cost 1100 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] c556  BS[1] a761  BS[2] 9393  BS[3] fc03 , Prev_Value 6237 , Rem Cost 400 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 6237  BS[1] a761  BS[2] 9393  BS[3] fc03 , Prev_Value 589e , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 6237  BS[1] 589e  BS[2] 9393  BS[3] fc03 , Prev_Value 6c6c , Rem Cost 100 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[1];
X[3] = F[0];

// to : 6C6C FC03 589E 6237 
// T-Depth : 4
// Depth : 34
