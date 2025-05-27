// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[0];
F[3] = X[2];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 00ff  BS[3] cccc , Prev_Value 3333 , Rem Cost 100

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f5a  BS[1] 5555  BS[2] 00ff  BS[3] cccc , Prev_Value 0f0f , Rem Cost 800

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 5a0f  BS[2] 00ff  BS[3] cccc , Prev_Value 5555 , Rem Cost 1000

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f5a  BS[1] 5a0f  BS[2] cc33  BS[3] cccc , Prev_Value 00ff , Rem Cost 1200

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 5647  BS[2] cc33  BS[3] cccc , Prev_Value 5a0f , Rem Cost 1900

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f5a  BS[1] 5647  BS[2] cc33  BS[3] cccc , Prev_Value 8877 , Rem Cost 1900 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 5647  BS[2] 8877  BS[3] cccc , Prev_Value c49e , Rem Cost 1200 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 5647  BS[2] 8877  BS[3] c49e , Prev_Value 92d9 , Rem Cost 500 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 5647  BS[2] 8877  BS[3] 92d9 , Prev_Value de30 , Rem Cost 300 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f5a  BS[1] de30  BS[2] 8877  BS[3] 92d9 , Prev_Value 7788 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : 7788 0F5A 92D9 DE30 
// T-Depth : 4
// Depth : 35
