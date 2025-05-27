// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[0];
F[3] = X[3];

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 33cc  BS[1] 0f0f  BS[2] 00ff  BS[3] 5555 , Prev_Value 3333 , Rem Cost 200

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 33cc  BS[1] 0f0f  BS[2] 55aa  BS[3] 5555 , Prev_Value 00ff , Rem Cost 400

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 33cc  BS[1] 0f0f  BS[2] 55aa  BS[3] aaaa , Prev_Value 5555 , Rem Cost 500

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 33cc  BS[1] 3cc3  BS[2] 55aa  BS[3] aaaa , Prev_Value 0f0f , Rem Cost 700

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3366  BS[1] 3cc3  BS[2] 55aa  BS[3] aaaa , Prev_Value 33cc , Rem Cost 1400

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3366  BS[1] 3cc3  BS[2] 55aa  BS[3] 9ae8 , Prev_Value aaaa , Rem Cost 2100

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3366  BS[1] 3cc3  BS[2] 55aa  BS[3] 9ae8 , Prev_Value 47ca , Rem Cost 1900 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3366  BS[1] 3cc3  BS[2] 47ca  BS[3] 9ae8 , Prev_Value 0fa5 , Rem Cost 1200 R

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3366  BS[1] 0fa5  BS[2] 47ca  BS[3] 9ae8 , Prev_Value 34e6 , Rem Cost 1000 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 34e6  BS[1] 0fa5  BS[2] 47ca  BS[3] 9ae8 , Prev_Value cb19 , Rem Cost 300 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] cb19  BS[1] 0fa5  BS[2] 47ca  BS[3] 9ae8 , Prev_Value c4bc , Rem Cost 200 R


X[0] = F[1];
X[1] = F[0];
X[2] = F[2];
X[3] = F[3];

// to : C4BC CB19 47CA 9AE8 
// T-Depth : 4
// Depth : 38
