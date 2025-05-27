// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[3];
F[3] = X[0];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] 5555  BS[3] ff00 , Prev_Value 00ff , Rem Cost 100

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 3c0f  BS[2] 5555  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 800

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 3c0f  BS[2] 5555  BS[3] c30f , Prev_Value ff00 , Rem Cost 1000

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 3c0f  BS[2] 555a  BS[3] c30f , Prev_Value 5555 , Rem Cost 1700

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 3c0f  BS[2] 555a  BS[3] c30f , Prev_Value 2d1d , Rem Cost 1900 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 2d1d  BS[2] 555a  BS[3] c30f , Prev_Value 1e2e , Rem Cost 1200 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1e2e  BS[1] 2d1d  BS[2] 555a  BS[3] c30f , Prev_Value 6c17 , Rem Cost 1000 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1e2e  BS[1] 6c17  BS[2] 555a  BS[3] c30f , Prev_Value aaa5 , Rem Cost 300 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 1e2e  BS[1] 6c17  BS[2] aaa5  BS[3] c30f , Prev_Value 3cf0 , Rem Cost 200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 1e2e  BS[1] 6c17  BS[2] aaa5  BS[3] 3cf0 , Prev_Value 93e8 , Rem Cost 100 R


X[0] = F[3];
X[1] = F[2];
X[2] = F[1];
X[3] = F[0];

// to : 3CF0 AAA5 93E8 1E2E 
// T-Depth : 4
// Depth : 34
