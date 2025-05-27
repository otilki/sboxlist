// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[0];
F[2] = X[1];
F[3] = X[2];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 100

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] c3c3  BS[3] cccc , Prev_Value 0f0f , Rem Cost 300

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] c3c3  BS[3] cc99 , Prev_Value cccc , Rem Cost 1000

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 5555  BS[1] c33c  BS[2] c3c3  BS[3] cc99 , Prev_Value 00ff , Rem Cost 1200

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 954d  BS[1] c33c  BS[2] c3c3  BS[3] cc99 , Prev_Value 5555 , Rem Cost 1900

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 954d  BS[1] c33c  BS[2] c3c3  BS[3] cc99 , Prev_Value 47ca , Rem Cost 2000 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 954d  BS[1] c33c  BS[2] 47ca  BS[3] cc99 , Prev_Value 0fa5 , Rem Cost 1300 R

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 954d  BS[1] 0fa5  BS[2] 47ca  BS[3] cc99 , Prev_Value cb19 , Rem Cost 1100 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 954d  BS[1] 0fa5  BS[2] 47ca  BS[3] cb19 , Prev_Value 9ae8 , Rem Cost 400 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 9ae8  BS[1] 0fa5  BS[2] 47ca  BS[3] cb19 , Prev_Value c4bc , Rem Cost 200 R


X[0] = F[1];
X[1] = F[3];
X[2] = F[2];
X[3] = F[0];

// to : C4BC CB19 47CA 9AE8 
// T-Depth : 4
// Depth : 39
