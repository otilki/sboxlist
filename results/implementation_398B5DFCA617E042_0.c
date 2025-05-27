// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[0];
F[2] = X[3];
F[3] = X[2];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 00ff  BS[2] aaaa  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 22dd  BS[2] aaaa  BS[3] 3333 , Prev_Value 00ff , Rem Cost 800

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 22dd  BS[2] 8877  BS[3] 3333 , Prev_Value aaaa , Rem Cost 1000

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 22dd  BS[2] 8877  BS[3] bb44 , Prev_Value 3333 , Rem Cost 1200

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f5a  BS[1] 22dd  BS[2] 8877  BS[3] bb44 , Prev_Value 0f0f , Rem Cost 1900

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 22dd  BS[2] 8877  BS[3] bb44 , Prev_Value 299d , Rem Cost 1800 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 299d  BS[2] 8877  BS[3] bb44 , Prev_Value 92d9 , Rem Cost 1100 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 299d  BS[2] 8877  BS[3] 92d9 , Prev_Value 21cf , Rem Cost 900 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f5a  BS[1] 21cf  BS[2] 8877  BS[3] 92d9 , Prev_Value 7788 , Rem Cost 200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 21cf  BS[2] 7788  BS[3] 92d9 , Prev_Value de30 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : 7788 0F5A 92D9 DE30 
// T-Depth : 4
// Depth : 36
