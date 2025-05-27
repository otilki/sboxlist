// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[0];
F[2] = X[3];
F[3] = X[2];

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5555  BS[3] 3333 , Prev_Value 00ff , Rem Cost 200

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 33cc  BS[2] 5555  BS[3] 2277 , Prev_Value 3333 , Rem Cost 900

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] cc33  BS[2] 5555  BS[3] 2277 , Prev_Value 33cc , Rem Cost 1000

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] cc33  BS[2] aaaa  BS[3] 2277 , Prev_Value 5555 , Rem Cost 1100

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2d78  BS[1] cc33  BS[2] aaaa  BS[3] 2277 , Prev_Value 0f0f , Rem Cost 1300

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2d78  BS[1] cc33  BS[2] aaaa  BS[3] ee44 , Prev_Value 2277 , Rem Cost 1500

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2d78  BS[1] cc33  BS[2] 87d2  BS[3] ee44 , Prev_Value aaaa , Rem Cost 1700

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2d78  BS[1] 4be1  BS[2] 87d2  BS[3] ee44 , Prev_Value cc33 , Rem Cost 1900

F[1] = CCCNOT2(F[0], F[2], F[3], F[1]);
Info_Op:  , Info_Line: 1, Op_Values  BS[0] 2d78  BS[1] 4fa1  BS[2] 87d2  BS[3] ee44 , Prev_Value 4be1 , Rem Cost 4000

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2d78  BS[1] 4fa1  BS[2] 87d2  BS[3] ee44 , Prev_Value 6378 , Rem Cost 2600 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] 87d2  BS[3] ee44 , Prev_Value ed14 , Rem Cost 1900 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] 87d2  BS[3] ed14 , Prev_Value 6ac6 , Rem Cost 1200 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] 87d2  BS[3] 6ac6 , Prev_Value e592 , Rem Cost 1000 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 6378  BS[1] 4fa1  BS[2] e592  BS[3] 6ac6 , Prev_Value 2cd9 , Rem Cost 300 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 6378  BS[1] 2cd9  BS[2] e592  BS[3] 6ac6 , Prev_Value 1a6d , Rem Cost 100 R


X[0] = F[2];
X[1] = F[1];
X[2] = F[3];
X[3] = F[0];

// to : 1A6D 2CD9 6AC6 6378 
// T-Depth : 7
// Depth : 61
