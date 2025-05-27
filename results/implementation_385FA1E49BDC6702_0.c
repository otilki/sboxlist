// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[0];
F[3] = X[3];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] ff00  BS[3] 5555 , Prev_Value 00ff , Rem Cost 100

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5a0f  BS[2] ff00  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 800

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5a0f  BS[2] a50f  BS[3] 5555 , Prev_Value ff00 , Rem Cost 1000

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a0f  BS[2] a50f  BS[3] f05a , Prev_Value 5555 , Rem Cost 1200

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 333c  BS[1] 5a0f  BS[2] a50f  BS[3] f05a , Prev_Value 3333 , Rem Cost 1900

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 333c  BS[1] 5a0f  BS[2] a50f  BS[3] f05a , Prev_Value d156 , Rem Cost 1800 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 5a0f  BS[2] a50f  BS[3] d156 , Prev_Value 4b1b , Rem Cost 1100 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 333c  BS[1] 4b1b  BS[2] a50f  BS[3] d156 , Prev_Value 9a4d , Rem Cost 400 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 333c  BS[1] 4b1b  BS[2] a50f  BS[3] 9a4d , Prev_Value 5af0 , Rem Cost 200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 4b1b  BS[2] 5af0  BS[3] 9a4d , Prev_Value b4e4 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : 5AF0 333C 9A4D B4E4 
// T-Depth : 4
// Depth : 36
