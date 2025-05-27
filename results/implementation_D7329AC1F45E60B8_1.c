// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[3];
F[3] = X[0];

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] 55aa  BS[3] 00ff , Prev_Value 5555 , Rem Cost 200

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] 55aa  BS[3] 03fc , Prev_Value 00ff , Rem Cost 900

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 329b  BS[1] 0f0f  BS[2] 55aa  BS[3] 03fc , Prev_Value 3333 , Rem Cost 1600

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 329b  BS[1] 0f0f  BS[2] 55aa  BS[3] fc03 , Prev_Value 03fc , Rem Cost 1700

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 329b  BS[1] 0f0f  BS[2] 55aa  BS[3] f30c , Prev_Value fc03 , Rem Cost 1900

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 329b  BS[1] 3d07  BS[2] 55aa  BS[3] f30c , Prev_Value 0f0f , Rem Cost 2600

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 329b  BS[1] 3d07  BS[2] 55aa  BS[3] f30c , Prev_Value 6731 , Rem Cost 2100 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 329b  BS[1] 3d07  BS[2] 6731  BS[3] f30c , Prev_Value ce0b , Rem Cost 1900 R

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 329b  BS[1] 3d07  BS[2] 6731  BS[3] ce0b , Prev_Value 749a , Rem Cost 1700 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 749a  BS[1] 3d07  BS[2] 6731  BS[3] ce0b , Prev_Value c2f8 , Rem Cost 1000 R

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 749a  BS[1] c2f8  BS[2] 6731  BS[3] ce0b , Prev_Value 8e93 , Rem Cost 900 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 749a  BS[1] c2f8  BS[2] 6731  BS[3] 8e93 , Prev_Value e9a2 , Rem Cost 200 R


X[0] = F[3];
X[1] = F[1];
X[2] = F[0];
X[3] = F[2];

// to : 8E93 C2F8 749A E9A2 
// T-Depth : 5
// Depth : 44
