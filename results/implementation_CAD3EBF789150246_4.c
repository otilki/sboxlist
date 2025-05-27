// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[3];
F[3] = X[0];

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] 5555  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 1

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 2

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] 5555  BS[3] af50 , Prev_Value ff00 , Rem Cost 102

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] 5f05  BS[3] af50 , Prev_Value 5555 , Rem Cost 202

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] 5f05  BS[3] 9c63 , Prev_Value af50 , Rem Cost 203

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] 5f05  BS[3] 9c63 , Prev_Value 055f , Rem Cost 203 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 055f  BS[2] 5f05  BS[3] 9c63 , Prev_Value 3770 , Rem Cost 202 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3770  BS[1] 055f  BS[2] 5f05  BS[3] 9c63 , Prev_Value 113f , Rem Cost 102 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3770  BS[1] 113f  BS[2] 5f05  BS[3] 9c63 , Prev_Value eec0 , Rem Cost 2 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3770  BS[1] eec0  BS[2] 5f05  BS[3] 9c63 , Prev_Value ab13 , Rem Cost 1 R


X[0] = F[1];
X[1] = F[3];
X[2] = F[2];
X[3] = F[0];

// to : EEC0 AB13 5F05 3770 
// T-Depth : 4
// Depth : 34
