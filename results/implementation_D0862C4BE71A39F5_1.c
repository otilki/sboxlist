// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[0];
F[2] = X[2];
F[3] = X[3];

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f5a  BS[1] 00ff  BS[2] 3333  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 700

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 00ff  BS[2] 3333  BS[3] aaaa , Prev_Value 5555 , Rem Cost 800

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f5a  BS[1] 00ff  BS[2] 9999  BS[3] aaaa , Prev_Value 3333 , Rem Cost 1000

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 00ff  BS[2] 9999  BS[3] a5f0 , Prev_Value aaaa , Rem Cost 1200

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f5a  BS[1] 816f  BS[2] 9999  BS[3] a5f0 , Prev_Value 00ff , Rem Cost 1900

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 816f  BS[2] 9999  BS[3] a5f0 , Prev_Value 24f9 , Rem Cost 1800 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f5a  BS[1] 816f  BS[2] 9999  BS[3] 24f9 , Prev_Value a596 , Rem Cost 1100 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0f5a  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value 96c3 , Rem Cost 900 R

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 96c3  BS[1] 816f  BS[2] 9999  BS[3] a596 , Prev_Value 19da , Rem Cost 700 R


X[0] = F[3];
X[1] = F[0];
X[2] = F[2];
X[3] = F[1];

// to : A596 96C3 19DA 816F 
// T-Depth : 4
// Depth : 35
