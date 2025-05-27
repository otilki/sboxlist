// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[0];
F[3] = X[1];

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 5555  BS[2] 00ff  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 200

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 5959  BS[2] 00ff  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 900

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 5959  BS[2] 00ff  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1000

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] 00ff  BS[3] f0f0 , Prev_Value 3c3c , Rem Cost 1700

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] ff00  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 1800

F[2] = CCCNOT2(F[0], F[1], F[3], F[2]);
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] ef40  BS[3] f0f0 , Prev_Value ff00 , Rem Cost 3900

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] 5959  BS[2] ef40  BS[3] f0f0 , Prev_Value b619 , Rem Cost 2100 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] b619  BS[2] ef40  BS[3] f0f0 , Prev_Value 46e9 , Rem Cost 1900 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] b619  BS[2] ef40  BS[3] 46e9 , Prev_Value 9a59 , Rem Cost 1700 R

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 9a59  BS[2] ef40  BS[3] 46e9 , Prev_Value ed09 , Rem Cost 1000 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c65  BS[1] 9a59  BS[2] ed09  BS[3] 46e9 , Prev_Value d16c , Rem Cost 300 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] 9a59  BS[2] d16c  BS[3] 46e9 , Prev_Value b916 , Rem Cost 100 R


X[0] = F[3];
X[1] = F[2];
X[2] = F[0];
X[3] = F[1];

// to : B916 D16C 3C65 9A59 
// T-Depth : 7
// Depth : 58
