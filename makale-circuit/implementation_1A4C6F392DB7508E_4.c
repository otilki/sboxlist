// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[1];
F[3] = X[0];

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 5555  BS[1] 3636  BS[2] 0f0f  BS[3] 00ff , Prev_Value 3333 , Rem Cost 700

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 5563  BS[1] 3636  BS[2] 0f0f  BS[3] 00ff , Prev_Value 5555 , Rem Cost 1400

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5563  BS[1] 3636  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 1500

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 5563  BS[1] c9c9  BS[2] 0f0f  BS[3] ff00 , Prev_Value 3636 , Rem Cost 1600

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aa9c  BS[1] c9c9  BS[2] 0f0f  BS[3] ff00 , Prev_Value 5563 , Rem Cost 1700

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] aa9c  BS[1] c9c9  BS[2] f0f0  BS[3] ff00 , Prev_Value 0f0f , Rem Cost 1800

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] aa9c  BS[1] c9c9  BS[2] f0f0  BS[3] ff00 , Prev_Value 7878 , Rem Cost 1900 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] aa9c  BS[1] c9c9  BS[2] 7878  BS[3] ff00 , Prev_Value 8778 , Rem Cost 1200 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] aa9c  BS[1] c9c9  BS[2] 7878  BS[3] 8778 , Prev_Value 4eb1 , Rem Cost 1000 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aa9c  BS[1] 4eb1  BS[2] 7878  BS[3] 8778 , Prev_Value 5563 , Rem Cost 800 R

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 5563  BS[1] 4eb1  BS[2] 7878  BS[3] 8778 , Prev_Value 3c59 , Rem Cost 700 R


X[0] = F[0];
X[1] = F[2];
X[2] = F[1];
X[3] = F[3];

// to : 5563 3C59 4EB1 8778 
// T-Depth : 4
// Depth : 33
