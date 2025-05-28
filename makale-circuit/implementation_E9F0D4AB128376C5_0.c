// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[1];
F[3] = X[0];

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 3333  BS[2] 0f0f  BS[3] 00ff , Prev_Value 5555 , Rem Cost 100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] 3333  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 200

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] 3333  BS[2] f0f0  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 300

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] c333  BS[2] f0f0  BS[3] ff00 , Prev_Value 3333 , Rem Cost 1000

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 6999  BS[1] c333  BS[2] f0f0  BS[3] ff00 , Prev_Value aaaa , Rem Cost 1200

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 6999  BS[1] a3a3  BS[2] f0f0  BS[3] ff00 , Prev_Value c333 , Rem Cost 1900

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6999  BS[1] a3a3  BS[2] f0f0  BS[3] ff00 , Prev_Value 53f0 , Rem Cost 1800 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 6999  BS[1] a3a3  BS[2] 53f0  BS[3] ff00 , Prev_Value 5ca3 , Rem Cost 1100 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 6999  BS[1] a3a3  BS[2] 53f0  BS[3] 5ca3 , Prev_Value eb22 , Rem Cost 900 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 6999  BS[1] eb22  BS[2] 53f0  BS[3] 5ca3 , Prev_Value a35c , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 6999  BS[1] eb22  BS[2] 53f0  BS[3] a35c , Prev_Value ac0f , Rem Cost 100 R


X[0] = F[1];
X[1] = F[2];
X[2] = F[3];
X[3] = F[0];

// to : EB22 AC0F A35C 6999 
// T-Depth : 4
// Depth : 34
