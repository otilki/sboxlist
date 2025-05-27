// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[1];
F[3] = X[3];

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 03fc  BS[1] 3333  BS[2] 0f0f  BS[3] 5555 , Prev_Value 00ff , Rem Cost 700

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 03fc  BS[1] 3333  BS[2] 3c3c  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 900

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 03fc  BS[1] 3333  BS[2] 3d68  BS[3] 5555 , Prev_Value 3c3c , Rem Cost 1600

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 03fc  BS[1] 2673  BS[2] 3d68  BS[3] 5555 , Prev_Value 3333 , Rem Cost 2300

F[0] = CCCNOT2(F[1], F[2], F[3], F[0]);
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 03fc  BS[1] 2673  BS[2] 3d68  BS[3] 5555 , Prev_Value 07bc , Rem Cost 3700 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 07bc  BS[1] 2673  BS[2] 3d68  BS[3] 5555 , Prev_Value 52e9 , Rem Cost 1600 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 07bc  BS[1] 2673  BS[2] 3d68  BS[3] 52e9 , Prev_Value 3ad4 , Rem Cost 1400 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 3ad4  BS[1] 2673  BS[2] 3d68  BS[3] 52e9 , Prev_Value c52b , Rem Cost 1200 R

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] c52b  BS[1] 2673  BS[2] 3d68  BS[3] 52e9 , Prev_Value 394b , Rem Cost 1100 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] c52b  BS[1] 2673  BS[2] 394b  BS[3] 52e9 , Prev_Value 749a , Rem Cost 400 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] c52b  BS[1] 749a  BS[2] 394b  BS[3] 52e9 , Prev_Value 97c2 , Rem Cost 200 R


X[0] = F[0];
X[1] = F[1];
X[2] = F[3];
X[3] = F[2];

// to : 97C2 749A 52E9 394B 
// T-Depth : 7
// Depth : 60
