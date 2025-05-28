// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[0];
F[2] = X[3];
F[3] = X[1];

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 00ff  BS[2] 555a  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 700

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 0ff0  BS[2] 555a  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 900

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 0ff0  BS[2] 555a  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 1000

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 3fc0  BS[2] 555a  BS[3] f0f0 , Prev_Value 0ff0 , Rem Cost 1700

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3333  BS[1] 3fc0  BS[2] 555a  BS[3] f0f0 , Prev_Value 2673 , Rem Cost 1700 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 2673  BS[1] 3fc0  BS[2] 555a  BS[3] f0f0 , Prev_Value aaa5 , Rem Cost 1000 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 2673  BS[1] 3fc0  BS[2] aaa5  BS[3] f0f0 , Prev_Value d2d1 , Rem Cost 900 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2673  BS[1] 3fc0  BS[2] aaa5  BS[3] d2d1 , Prev_Value 8cd6 , Rem Cost 200 R


X[0] = F[1];
X[1] = F[3];
X[2] = F[0];
X[3] = F[2];

// to : 3FC0 D2D1 8CD6 AAA5 
// T-Depth : 4
// Depth : 34
