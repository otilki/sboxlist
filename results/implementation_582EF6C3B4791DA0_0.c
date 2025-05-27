// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[0];
F[2] = X[1];
F[3] = X[2];

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 5566  BS[1] 00ff  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 700

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 5566  BS[1] 5599  BS[2] 0f0f  BS[3] 3333 , Prev_Value 00ff , Rem Cost 900

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5566  BS[1] 5599  BS[2] 0f0f  BS[3] 6655 , Prev_Value 3333 , Rem Cost 1100

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5566  BS[1] 5599  BS[2] 5a96  BS[3] 6655 , Prev_Value 0f0f , Rem Cost 1300

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 1177  BS[1] 5599  BS[2] 5a96  BS[3] 6655 , Prev_Value 5566 , Rem Cost 2000

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 1177  BS[1] 5599  BS[2] 5a96  BS[3] 6655 , Prev_Value 7643 , Rem Cost 2000 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1177  BS[1] 5599  BS[2] 5a96  BS[3] 7643 , Prev_Value 6734 , Rem Cost 1300 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 6734  BS[1] 5599  BS[2] 5a96  BS[3] 7643 , Prev_Value 3da2 , Rem Cost 1100 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3da2  BS[1] 5599  BS[2] 5a96  BS[3] 7643 , Prev_Value 619b , Rem Cost 900 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3da2  BS[1] 619b  BS[2] 5a96  BS[3] 7643 , Prev_Value 89bc , Rem Cost 200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3da2  BS[1] 619b  BS[2] 5a96  BS[3] 89bc , Prev_Value 9e64 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[1];
X[2] = F[0];
X[3] = F[3];

// to : 5A96 9E64 3DA2 89BC 
// T-Depth : 4
// Depth : 37
