// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[0];
F[3] = X[1];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] ff00  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 100

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5a55  BS[2] ff00  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 800

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5a55  BS[2] a555  BS[3] 0f0f , Prev_Value ff00 , Rem Cost 1000

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a55  BS[2] a555  BS[3] aa5a , Prev_Value 0f0f , Rem Cost 1200

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3366  BS[1] 5a55  BS[2] a555  BS[3] aa5a , Prev_Value 3333 , Rem Cost 1900

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3366  BS[1] 5a55  BS[2] a555  BS[3] aa5a , Prev_Value 8b1e , Rem Cost 1800 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3366  BS[1] 5a55  BS[2] a555  BS[3] 8b1e , Prev_Value 5953 , Rem Cost 1100 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3366  BS[1] 5953  BS[2] a555  BS[3] 8b1e , Prev_Value d24d , Rem Cost 400 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3366  BS[1] 5953  BS[2] a555  BS[3] d24d , Prev_Value 5aaa , Rem Cost 200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3366  BS[1] 5953  BS[2] 5aaa  BS[3] d24d , Prev_Value a6ac , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : 5AAA 3366 D24D A6AC 
// T-Depth : 4
// Depth : 36
