// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[0];
F[2] = X[1];
F[3] = X[3];

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3366  BS[1] 00ff  BS[2] 0f0f  BS[3] 5555 , Prev_Value 3333 , Rem Cost 700

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3366  BS[1] 3399  BS[2] 0f0f  BS[3] 5555 , Prev_Value 00ff , Rem Cost 900

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3366  BS[1] 66cc  BS[2] 0f0f  BS[3] 5555 , Prev_Value 3399 , Rem Cost 1100

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3366  BS[1] 66cc  BS[2] 69c3  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 1300

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3366  BS[1] 66cc  BS[2] 69c3  BS[3] 7711 , Prev_Value 5555 , Rem Cost 2000

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3366  BS[1] 66cc  BS[2] 69c3  BS[3] 7711 , Prev_Value 5267 , Rem Cost 2000 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5267  BS[1] 66cc  BS[2] 69c3  BS[3] 7711 , Prev_Value 1ed2 , Rem Cost 1300 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5267  BS[1] 66cc  BS[2] 69c3  BS[3] 1ed2 , Prev_Value 4cb5 , Rem Cost 1100 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 5267  BS[1] 66cc  BS[2] 69c3  BS[3] 4cb5 , Prev_Value 26e9 , Rem Cost 900 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 5267  BS[1] 26e9  BS[2] 69c3  BS[3] 4cb5 , Prev_Value ad98 , Rem Cost 200 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] ad98  BS[1] 26e9  BS[2] 69c3  BS[3] 4cb5 , Prev_Value b34a , Rem Cost 100 R


X[0] = F[2];
X[1] = F[1];
X[2] = F[0];
X[3] = F[3];

// to : 69C3 26E9 AD98 B34A 
// T-Depth : 4
// Depth : 39
