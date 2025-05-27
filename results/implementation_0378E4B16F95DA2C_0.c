// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[1];
F[3] = X[0];

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 5555  BS[1] 33cc  BS[2] 0f0f  BS[3] 00ff , Prev_Value 3333 , Rem Cost 200

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 33cc  BS[2] 0f0f  BS[3] ff00 , Prev_Value 00ff , Rem Cost 300

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 33cc  BS[2] 0f0f  BS[3] ee44 , Prev_Value ff00 , Rem Cost 1000

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] bb11  BS[1] 33cc  BS[2] 0f0f  BS[3] ee44 , Prev_Value 5555 , Rem Cost 1200

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] bb11  BS[1] 33cc  BS[2] b41e  BS[3] ee44 , Prev_Value 0f0f , Rem Cost 1400

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] bb11  BS[1] 87d2  BS[2] b41e  BS[3] ee44 , Prev_Value 33cc , Rem Cost 1600

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3cc3  BS[1] 87d2  BS[2] b41e  BS[3] ee44 , Prev_Value bb11 , Rem Cost 1800

F[2] = CCCNOT2(F[0], F[1], F[3], F[2]);
Info_Op:  , Info_Line: 2, Op_Values  BS[0] 3cc3  BS[1] 87d2  BS[2] b05e  BS[3] ee44 , Prev_Value b41e , Rem Cost 3900

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3cc3  BS[1] 87d2  BS[2] b05e  BS[3] ee44 , Prev_Value 9c87 , Rem Cost 2500 R

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 9c87  BS[1] 87d2  BS[2] b05e  BS[3] ee44 , Prev_Value 6ac6 , Rem Cost 1800 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 9c87  BS[1] 87d2  BS[2] b05e  BS[3] 6ac6 , Prev_Value 2cd9 , Rem Cost 1100 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 9c87  BS[1] 87d2  BS[2] 2cd9  BS[3] 6ac6 , Prev_Value 6378 , Rem Cost 900 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 6378  BS[1] 87d2  BS[2] 2cd9  BS[3] 6ac6 , Prev_Value e592 , Rem Cost 800 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 6378  BS[1] e592  BS[2] 2cd9  BS[3] 6ac6 , Prev_Value 1a6d , Rem Cost 100 R


X[0] = F[1];
X[1] = F[2];
X[2] = F[3];
X[3] = F[0];

// to : 1A6D 2CD9 6AC6 6378 
// T-Depth : 7
// Depth : 64
