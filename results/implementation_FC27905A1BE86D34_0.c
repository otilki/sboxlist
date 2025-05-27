// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[3];
F[3] = X[1];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 200

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] d2d2 , Prev_Value f0f0 , Rem Cost 900

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 33cc  BS[2] aaaa  BS[3] d2d2 , Prev_Value 3333 , Rem Cost 1100

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 9966  BS[2] aaaa  BS[3] d2d2 , Prev_Value 33cc , Rem Cost 1300

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 9966  BS[2] aacc  BS[3] d2d2 , Prev_Value aaaa , Rem Cost 2000

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 9966  BS[2] aacc  BS[3] d2d2 , Prev_Value 1ba6 , Rem Cost 2000 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 1ba6  BS[2] aacc  BS[3] d2d2 , Prev_Value d22d , Rem Cost 1300 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] d22d  BS[1] 1ba6  BS[2] aacc  BS[3] d2d2 , Prev_Value b16a , Rem Cost 1100 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] d22d  BS[1] 1ba6  BS[2] b16a  BS[3] d2d2 , Prev_Value c974 , Rem Cost 900 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] d22d  BS[1] 1ba6  BS[2] b16a  BS[3] c974 , Prev_Value 9ac6 , Rem Cost 700 R


X[0] = F[3];
X[1] = F[0];
X[2] = F[2];
X[3] = F[1];

// to : C974 D22D B16A 9AC6 
// T-Depth : 4
// Depth : 37
