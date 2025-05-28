// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[0];
F[3] = X[1];

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] cccc  BS[1] 5555  BS[2] 00ff  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 100

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] cccc  BS[1] 5555  BS[2] ff00  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 200

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] cccc  BS[1] 5555  BS[2] ff00  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 300

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3ccc  BS[1] 5555  BS[2] ff00  BS[3] f0f0 , Prev_Value cccc , Rem Cost 1000

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3ccc  BS[1] 5555  BS[2] aa55  BS[3] f0f0 , Prev_Value ff00 , Rem Cost 1200

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3ccc  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value 5555 , Rem Cost 1400

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 14dd  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value 3ccc , Rem Cost 2100

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 14dd  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value eb22 , Rem Cost 1600 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] eb22  BS[1] 6999  BS[2] aa55  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1500 R

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] eb22  BS[1] 6999  BS[2] aa55  BS[3] 0f0f , Prev_Value a35c , Rem Cost 1400 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] eb22  BS[1] 6999  BS[2] a35c  BS[3] 0f0f , Prev_Value ac0f , Rem Cost 700 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[2];
X[3] = F[1];

// to : EB22 AC0F A35C 6999 
// T-Depth : 4
// Depth : 33
