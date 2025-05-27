// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[2];
F[3] = X[1];

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3333  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] a9a9  BS[2] 3333  BS[3] 0f0f , Prev_Value aaaa , Rem Cost 800

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] a9a9  BS[2] 3333  BS[3] a6a6 , Prev_Value 0f0f , Rem Cost 1000

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] a659  BS[1] a9a9  BS[2] 3333  BS[3] a6a6 , Prev_Value 00ff , Rem Cost 1200

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] a659  BS[1] a9a9  BS[2] 933a  BS[3] a6a6 , Prev_Value 3333 , Rem Cost 1900

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] a659  BS[1] 3a93  BS[2] 933a  BS[3] a6a6 , Prev_Value a9a9 , Rem Cost 2100

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 247b  BS[1] 3a93  BS[2] 933a  BS[3] a6a6 , Prev_Value a659 , Rem Cost 2800

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 247b  BS[1] 3a93  BS[2] 933a  BS[3] a6a6 , Prev_Value 86b5 , Rem Cost 2100 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 247b  BS[1] 3a93  BS[2] 933a  BS[3] 86b5 , Prev_Value 158f , Rem Cost 1400 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 247b  BS[1] 3a93  BS[2] 158f  BS[3] 86b5 , Prev_Value a2ce , Rem Cost 1200 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] a2ce  BS[1] 3a93  BS[2] 158f  BS[3] 86b5 , Prev_Value 863b , Rem Cost 1000 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] a2ce  BS[1] 3a93  BS[2] 158f  BS[3] 863b , Prev_Value 985d , Rem Cost 300 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 985d  BS[1] 3a93  BS[2] 158f  BS[3] 863b , Prev_Value 67a2 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[2];
X[2] = F[1];
X[3] = F[3];

// to : 67A2 158F 3A93 863B 
// T-Depth : 5
// Depth : 49
