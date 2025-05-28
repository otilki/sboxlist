// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[0];
F[3] = X[2];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] 00ff  BS[3] cccc , Prev_Value 3333 , Rem Cost 100

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 555a  BS[2] 00ff  BS[3] cccc , Prev_Value 5555 , Rem Cost 800

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 555a  BS[2] cc33  BS[3] cccc , Prev_Value 00ff , Rem Cost 1000

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 555a  BS[2] c03f  BS[3] cccc , Prev_Value cc33 , Rem Cost 1700

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 555a  BS[2] c03f  BS[3] cccc , Prev_Value 8cd6 , Rem Cost 1800 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 555a  BS[2] c03f  BS[3] 8cd6 , Prev_Value 5a55 , Rem Cost 1100 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 5a55  BS[1] 555a  BS[2] c03f  BS[3] 8cd6 , Prev_Value aaa5 , Rem Cost 900 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 5a55  BS[1] aaa5  BS[2] c03f  BS[3] 8cd6 , Prev_Value d2d1 , Rem Cost 800 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] d2d1  BS[1] aaa5  BS[2] c03f  BS[3] 8cd6 , Prev_Value 3fc0 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : 3FC0 D2D1 8CD6 AAA5 
// T-Depth : 4
// Depth : 33
