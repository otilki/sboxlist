// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[3];
F[3] = X[0];

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] 6666  BS[3] 00ff , Prev_Value 5555 , Rem Cost 200

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 333c  BS[1] 0f0f  BS[2] 6666  BS[3] 00ff , Prev_Value 3333 , Rem Cost 900

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 0ff0  BS[2] 6666  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 1100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 333c  BS[1] 0ff0  BS[2] 6666  BS[3] ff00 , Prev_Value 00ff , Rem Cost 1200

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 333c  BS[1] 3ccc  BS[2] 6666  BS[3] ff00 , Prev_Value 0ff0 , Rem Cost 1400

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 1778  BS[1] 3ccc  BS[2] 6666  BS[3] ff00 , Prev_Value 333c , Rem Cost 2100

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 1778  BS[1] 3ccc  BS[2] 6666  BS[3] ff00 , Prev_Value eb48 , Rem Cost 2000 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 1778  BS[1] 3ccc  BS[2] 6666  BS[3] eb48 , Prev_Value 9999 , Rem Cost 1300 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 1778  BS[1] 3ccc  BS[2] 9999  BS[3] eb48 , Prev_Value a555 , Rem Cost 1200 R

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 1778  BS[1] a555  BS[2] 9999  BS[3] eb48 , Prev_Value 38d9 , Rem Cost 1000 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 1778  BS[1] a555  BS[2] 38d9  BS[3] eb48 , Prev_Value 2fa1 , Rem Cost 300 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 2fa1  BS[1] a555  BS[2] 38d9  BS[3] eb48 , Prev_Value 5aaa , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : 38D9 2FA1 EB48 5AAA 
// T-Depth : 4
// Depth : 38
