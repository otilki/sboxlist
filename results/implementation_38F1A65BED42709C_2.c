// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[2];
F[2] = X[3];
F[3] = X[0];

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] 00ff , Prev_Value 5555 , Rem Cost 200

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] 55aa  BS[3] ff00 , Prev_Value 00ff , Rem Cost 300

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] f0f0  BS[1] 3333  BS[2] 55aa  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 400

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] f0f0  BS[1] 3333  BS[2] 55aa  BS[3] ee22 , Prev_Value ff00 , Rem Cost 1100

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] f0f0  BS[1] c3c3  BS[2] 55aa  BS[3] ee22 , Prev_Value 3333 , Rem Cost 1300

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] f0f0  BS[1] c3c3  BS[2] bb88  BS[3] ee22 , Prev_Value 55aa , Rem Cost 1500

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ed2  BS[1] c3c3  BS[2] bb88  BS[3] ee22 , Prev_Value f0f0 , Rem Cost 1700

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] bb88  BS[3] ee22 , Prev_Value c3c3 , Rem Cost 2400

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] bb88  BS[3] ee22 , Prev_Value b34a , Rem Cost 1800 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] b34a  BS[3] ee22 , Prev_Value 87e1 , Rem Cost 1100 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1ed2  BS[1] 69c3  BS[2] b34a  BS[3] 87e1 , Prev_Value ad98 , Rem Cost 900 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] ad98  BS[1] 69c3  BS[2] b34a  BS[3] 87e1 , Prev_Value 26e9 , Rem Cost 700 R


X[0] = F[1];
X[1] = F[3];
X[2] = F[0];
X[3] = F[2];

// to : 69C3 26E9 AD98 B34A 
// T-Depth : 4
// Depth : 37
