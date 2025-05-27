// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[0];
F[3] = X[3];

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] 03fc  BS[3] 5555 , Prev_Value 00ff , Rem Cost 700

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3267  BS[1] 0f0f  BS[2] 03fc  BS[3] 5555 , Prev_Value 3333 , Rem Cost 1400

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3267  BS[1] 3d68  BS[2] 03fc  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 1600

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3267  BS[1] 3d68  BS[2] 3e94  BS[3] 5555 , Prev_Value 03fc , Rem Cost 1800

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3e94  BS[3] 5555 , Prev_Value 3267 , Rem Cost 2500

F[2] = CCCNOT2(F[0], F[1], F[3], F[2]);
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3e94  BS[3] 5555 , Prev_Value 3ad4 , Rem Cost 3600 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3ad4  BS[3] 5555 , Prev_Value 683d , Rem Cost 1500 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3ad4  BS[3] 683d , Prev_Value 97c2 , Rem Cost 1300 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] 3ad4  BS[3] 97c2 , Prev_Value c52b , Rem Cost 1200 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 2673  BS[1] 3d68  BS[2] c52b  BS[3] 97c2 , Prev_Value 394b , Rem Cost 1100 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 394b  BS[2] c52b  BS[3] 97c2 , Prev_Value 52e9 , Rem Cost 400 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2673  BS[1] 394b  BS[2] 52e9  BS[3] 97c2 , Prev_Value 749a , Rem Cost 200 R


X[0] = F[3];
X[1] = F[0];
X[2] = F[2];
X[3] = F[1];

// to : 97C2 749A 52E9 394B 
// T-Depth : 7
// Depth : 59
