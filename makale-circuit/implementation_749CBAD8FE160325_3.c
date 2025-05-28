// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aaaa  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] aaa5  BS[3] 3333 , Prev_Value aaaa , Rem Cost 800

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 2d2e  BS[2] aaa5  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 1500

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 2d2e  BS[2] aaa5  BS[3] cccc , Prev_Value 3333 , Rem Cost 1600

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 2d2e  BS[2] 555a  BS[3] cccc , Prev_Value aaa5 , Rem Cost 1700

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 2d2e  BS[2] 555a  BS[3] cccc , Prev_Value d2d1 , Rem Cost 1700 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] d2d1  BS[2] 555a  BS[3] cccc , Prev_Value c03f , Rem Cost 1600 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] c03f  BS[1] d2d1  BS[2] 555a  BS[3] cccc , Prev_Value 8cd6 , Rem Cost 900 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] c03f  BS[1] d2d1  BS[2] 555a  BS[3] 8cd6 , Prev_Value 3fc0 , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3fc0  BS[1] d2d1  BS[2] 555a  BS[3] 8cd6 , Prev_Value aaa5 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[1];
X[2] = F[3];
X[3] = F[2];

// to : 3FC0 D2D1 8CD6 AAA5 
// T-Depth : 4
// Depth : 31
