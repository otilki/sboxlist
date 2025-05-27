// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[3];
F[3] = X[1];

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] 6666  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 200

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 33cc  BS[1] 3333  BS[2] 6666  BS[3] 0f0f , Prev_Value 00ff , Rem Cost 400

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 33cc  BS[1] 3c3c  BS[2] 6666  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 600

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 33cc  BS[1] 3c3c  BS[2] 6666  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 700

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 17e8  BS[1] 3c3c  BS[2] 6666  BS[3] f0f0 , Prev_Value 33cc , Rem Cost 1400

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 3c3c  BS[2] 7686  BS[3] f0f0 , Prev_Value 6666 , Rem Cost 2100

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 17e8  BS[1] 3c3c  BS[2] 7686  BS[3] f0f0 , Prev_Value e4d8 , Rem Cost 2100 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 17e8  BS[1] 3c3c  BS[2] 7686  BS[3] e4d8 , Prev_Value 58bc , Rem Cost 1400 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 58bc  BS[2] 7686  BS[3] e4d8 , Prev_Value 616e , Rem Cost 700 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 17e8  BS[1] 58bc  BS[2] 616e  BS[3] e4d8 , Prev_Value 9e91 , Rem Cost 500 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 17e8  BS[1] 58bc  BS[2] 9e91  BS[3] e4d8 , Prev_Value c62d , Rem Cost 400 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 17e8  BS[1] c62d  BS[2] 9e91  BS[3] e4d8 , Prev_Value 7a49 , Rem Cost 200 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[2];
X[3] = F[1];

// to : 17E8 7A49 9E91 C62D 
// T-Depth : 4
// Depth : 41
