// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[1];
F[3] = X[3];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] f0f0  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 100

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 3333  BS[2] f0f0  BS[3] 5555 , Prev_Value 00ff , Rem Cost 300

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 3333  BS[2] f0f0  BS[3] 4477 , Prev_Value 5555 , Rem Cost 1000

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] f0f0  BS[3] 4477 , Prev_Value 3333 , Rem Cost 1700

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] f0f0  BS[3] bb88 , Prev_Value 4477 , Rem Cost 1800

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] a55a  BS[3] bb88 , Prev_Value f0f0 , Rem Cost 2000

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 7343  BS[2] a55a  BS[3] bb88 , Prev_Value 26e9 , Rem Cost 2000 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 26e9  BS[1] 7343  BS[2] a55a  BS[3] bb88 , Prev_Value 1ed2 , Rem Cost 1800 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 26e9  BS[1] 7343  BS[2] 1ed2  BS[3] bb88 , Prev_Value 69c3 , Rem Cost 1600 R

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 26e9  BS[1] 69c3  BS[2] 1ed2  BS[3] bb88 , Prev_Value b34a , Rem Cost 900 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 26e9  BS[1] 69c3  BS[2] 1ed2  BS[3] b34a , Prev_Value ad98 , Rem Cost 200 R


X[0] = F[1];
X[1] = F[0];
X[2] = F[2];
X[3] = F[3];

// to : 69C3 26E9 AD98 B34A 
// T-Depth : 4
// Depth : 36
