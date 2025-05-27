// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[2];
F[2] = X[3];
F[3] = X[0];

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5555  BS[3] 00ff , Prev_Value 3333 , Rem Cost 200

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5599  BS[3] 00ff , Prev_Value 5555 , Rem Cost 900

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5599  BS[3] 05f6 , Prev_Value 00ff , Rem Cost 1600

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 506f  BS[3] 05f6 , Prev_Value 5599 , Rem Cost 1800

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 506f  BS[3] fa09 , Prev_Value 05f6 , Rem Cost 1900

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value 506f , Rem Cost 2100

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value 3d07 , Rem Cost 2500 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 3d07  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value c2f8 , Rem Cost 1800 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] c2f8  BS[1] 33cc  BS[2] 63a3  BS[3] fa09 , Prev_Value 716c , Rem Cost 1700 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] c2f8  BS[1] 716c  BS[2] 63a3  BS[3] fa09 , Prev_Value 8e93 , Rem Cost 1000 R

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] c2f8  BS[1] 8e93  BS[2] 63a3  BS[3] fa09 , Prev_Value e9a2 , Rem Cost 900 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] c2f8  BS[1] 8e93  BS[2] e9a2  BS[3] fa09 , Prev_Value 749a , Rem Cost 200 R


X[0] = F[1];
X[1] = F[0];
X[2] = F[3];
X[3] = F[2];

// to : 8E93 C2F8 749A E9A2 
// T-Depth : 5
// Depth : 45
