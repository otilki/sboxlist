// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[1];
F[3] = X[0];

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] aaaa  BS[2] 0f0f  BS[3] 00ff , Prev_Value 5555 , Rem Cost 100

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] aaaa  BS[2] 0f0f  BS[3] 03fc , Prev_Value 00ff , Rem Cost 800

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] aaaa  BS[2] f0f0  BS[3] 03fc , Prev_Value 0f0f , Rem Cost 900

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] cccc  BS[1] aaaa  BS[2] f0f0  BS[3] 03fc , Prev_Value 3333 , Rem Cost 1000

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] cccc  BS[1] aaaa  BS[2] f0f0  BS[3] fc03 , Prev_Value 03fc , Rem Cost 1100

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] f0f0  BS[3] fc03 , Prev_Value cccc , Rem Cost 1800

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] f0f0  BS[3] fc03 , Prev_Value 58f2 , Rem Cost 2000 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] 58f2  BS[3] fc03 , Prev_Value 349e , Rem Cost 1300 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 6c6c  BS[1] aaaa  BS[2] 349e  BS[3] fc03 , Prev_Value 56a9 , Rem Cost 1100 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 6c6c  BS[1] 56a9  BS[2] 349e  BS[3] fc03 , Prev_Value 6237 , Rem Cost 900 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6c6c  BS[1] 6237  BS[2] 349e  BS[3] fc03 , Prev_Value 589e , Rem Cost 700 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[2];
X[3] = F[1];

// to : 6C6C FC03 589E 6237 
// T-Depth : 4
// Depth : 33
