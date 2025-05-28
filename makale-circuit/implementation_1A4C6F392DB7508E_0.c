// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] cccc , Prev_Value 3333 , Rem Cost 100

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] c9c9 , Prev_Value cccc , Rem Cost 800

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 55aa  BS[3] c9c9 , Prev_Value 5555 , Rem Cost 1000

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 0ff0  BS[2] 55aa  BS[3] c9c9 , Prev_Value 0f0f , Rem Cost 1200

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0ff0  BS[2] 5563  BS[3] c9c9 , Prev_Value 55aa , Rem Cost 1900

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 0ff0  BS[2] 5563  BS[3] c9c9 , Prev_Value 4eb1 , Rem Cost 1900 R

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 4eb1  BS[2] 5563  BS[3] c9c9 , Prev_Value 44de , Rem Cost 1200 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 44de  BS[1] 4eb1  BS[2] 5563  BS[3] c9c9 , Prev_Value 8778 , Rem Cost 500 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 44de  BS[1] 4eb1  BS[2] 5563  BS[3] 8778 , Prev_Value c3a6 , Rem Cost 300 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] c3a6  BS[1] 4eb1  BS[2] 5563  BS[3] 8778 , Prev_Value 3c59 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[1];
X[3] = F[3];

// to : 5563 3C59 4EB1 8778 
// T-Depth : 4
// Depth : 38
