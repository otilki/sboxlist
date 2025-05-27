// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[1];
F[3] = X[0];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] f0f0  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 100

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] f0f0  BS[3] 00ff , Prev_Value 5555 , Rem Cost 300

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 55aa  BS[2] c3c3  BS[3] 00ff , Prev_Value f0f0 , Rem Cost 500

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] c3c3  BS[3] 00ff , Prev_Value 3333 , Rem Cost 1200

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] d263  BS[3] 00ff , Prev_Value c3c3 , Rem Cost 1900

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] d263  BS[3] d29c , Prev_Value 00ff , Rem Cost 2100

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 33f0  BS[1] 55aa  BS[2] d263  BS[3] d29c , Prev_Value 665a , Rem Cost 2000 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 33f0  BS[1] 665a  BS[2] d263  BS[3] d29c , Prev_Value b439 , Rem Cost 1800 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 33f0  BS[1] 665a  BS[2] b439  BS[3] d29c , Prev_Value 2d63 , Rem Cost 1600 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 33f0  BS[1] 665a  BS[2] b439  BS[3] 2d63 , Prev_Value cc0f , Rem Cost 1500 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] cc0f  BS[1] 665a  BS[2] b439  BS[3] 2d63 , Prev_Value 6a59 , Rem Cost 1400 R

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] cc0f  BS[1] 6a59  BS[2] b439  BS[3] 2d63 , Prev_Value ec16 , Rem Cost 700 R


X[0] = F[0];
X[1] = F[2];
X[2] = F[3];
X[3] = F[1];

// to : EC16 B439 2D63 6A59 
// T-Depth : 4
// Depth : 35
