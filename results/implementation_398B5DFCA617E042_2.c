// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[3];
F[3] = X[1];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 200

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 900

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0f0 , Prev_Value aaaa , Rem Cost 1100

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value f0f0 , Rem Cost 1800

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value b316 , Rem Cost 1900 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] b316  BS[2] 8877  BS[3] f0a5 , Prev_Value 92d9 , Rem Cost 1200 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 92d9  BS[1] b316  BS[2] 8877  BS[3] f0a5 , Prev_Value 21cf , Rem Cost 500 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 92d9  BS[1] 21cf  BS[2] 8877  BS[3] f0a5 , Prev_Value de30 , Rem Cost 300 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 92d9  BS[1] de30  BS[2] 8877  BS[3] f0a5 , Prev_Value 0f5a , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 92d9  BS[1] de30  BS[2] 8877  BS[3] 0f5a , Prev_Value 7788 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[0];
X[3] = F[1];

// to : 7788 0F5A 92D9 DE30 
// T-Depth : 4
// Depth : 34
