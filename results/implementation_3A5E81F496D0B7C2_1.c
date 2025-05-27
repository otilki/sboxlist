// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[2];
F[2] = X[3];
F[3] = X[0];

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5555  BS[3] 00ff , Prev_Value 3333 , Rem Cost 700

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 800

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] aa55  BS[3] ff00 , Prev_Value 5555 , Rem Cost 1000

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] a555  BS[3] ff00 , Prev_Value aa55 , Rem Cost 1700

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] a555  BS[3] ff00 , Prev_Value fc06 , Rem Cost 1900 R

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 3366  BS[2] a555  BS[3] fc06 , Prev_Value 2e4b , Rem Cost 1200 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2e4b  BS[1] 3366  BS[2] a555  BS[3] fc06 , Prev_Value d24d , Rem Cost 500 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] d24d  BS[1] 3366  BS[2] a555  BS[3] fc06 , Prev_Value 5aaa , Rem Cost 300 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] d24d  BS[1] 3366  BS[2] 5aaa  BS[3] fc06 , Prev_Value a6ac , Rem Cost 200 R


X[0] = F[2];
X[1] = F[1];
X[2] = F[0];
X[3] = F[3];

// to : 5AAA 3366 D24D A6AC 
// T-Depth : 4
// Depth : 35
