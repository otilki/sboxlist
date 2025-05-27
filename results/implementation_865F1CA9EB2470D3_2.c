// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[1];
F[3] = X[0];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 3c3c  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 300

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 3333  BS[2] 693c  BS[3] ff00 , Prev_Value 3c3c , Rem Cost 1000

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 7465  BS[1] 3333  BS[2] 693c  BS[3] ff00 , Prev_Value 5555 , Rem Cost 1700

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 7465  BS[1] 3333  BS[2] 693c  BS[3] 8b65 , Prev_Value ff00 , Rem Cost 1900

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 693c  BS[3] 8b65 , Prev_Value 7465 , Rem Cost 2100

F[2] = CCCNOT2(F[0], F[1], F[3], F[2]);
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 693c  BS[3] 8b65 , Prev_Value 683d , Rem Cost 3900 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 683d  BS[3] 8b65 , Prev_Value 97c2 , Rem Cost 1800 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1d59  BS[1] 3333  BS[2] 97c2  BS[3] 8b65 , Prev_Value 2673 , Rem Cost 1700 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 1d59  BS[1] 2673  BS[2] 97c2  BS[3] 8b65 , Prev_Value 749a , Rem Cost 1000 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 1d59  BS[1] 2673  BS[2] 97c2  BS[3] 749a , Prev_Value 394b , Rem Cost 900 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 394b  BS[1] 2673  BS[2] 97c2  BS[3] 749a , Prev_Value 52e9 , Rem Cost 200 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[1];
X[3] = F[0];

// to : 97C2 749A 52E9 394B 
// T-Depth : 7
// Depth : 58
