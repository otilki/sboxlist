// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[1];
F[3] = X[0];

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 0f3c  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 700

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 0f3c  BS[3] ff00 , Prev_Value 00ff , Rem Cost 800

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3627  BS[1] 5555  BS[2] 0f3c  BS[3] ff00 , Prev_Value 3333 , Rem Cost 1500

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3627  BS[1] 5555  BS[2] f0c3  BS[3] ff00 , Prev_Value 0f3c , Rem Cost 1600

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3627  BS[1] 5555  BS[2] f0c3  BS[3] ff00 , Prev_Value eb05 , Rem Cost 2100 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3627  BS[1] 5555  BS[2] f0c3  BS[3] eb05 , Prev_Value be50 , Rem Cost 1400 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3627  BS[1] be50  BS[2] f0c3  BS[3] eb05 , Prev_Value 8877 , Rem Cost 1200 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 8877  BS[1] be50  BS[2] f0c3  BS[3] eb05 , Prev_Value 6b46 , Rem Cost 1000 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 8877  BS[1] be50  BS[2] f0c3  BS[3] 6b46 , Prev_Value 7788 , Rem Cost 300 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 7788  BS[1] be50  BS[2] f0c3  BS[3] 6b46 , Prev_Value 0f3c , Rem Cost 200 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 7788  BS[1] be50  BS[2] 0f3c  BS[3] 6b46 , Prev_Value 94b9 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[2];
X[2] = F[3];
X[3] = F[1];

// to : 7788 0F3C 94B9 BE50 
// T-Depth : 4
// Depth : 33
