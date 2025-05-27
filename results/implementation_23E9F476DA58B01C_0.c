// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[2];
F[3] = X[3];

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 0f0f  BS[2] 3333  BS[3] 5555 , Prev_Value 00ff , Rem Cost 200

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0ff0  BS[1] 0f0f  BS[2] 3333  BS[3] 5aa5 , Prev_Value 5555 , Rem Cost 400

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0ff0  BS[1] 0c3f  BS[2] 3333  BS[3] 5aa5 , Prev_Value 0f0f , Rem Cost 1100

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 03cf  BS[1] 0c3f  BS[2] 3333  BS[3] 5aa5 , Prev_Value 0ff0 , Rem Cost 1300

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 03cf  BS[1] 0c3f  BS[2] 3b16  BS[3] 5aa5 , Prev_Value 3333 , Rem Cost 2000

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 03cf  BS[1] 0c3f  BS[2] 3b16  BS[3] 5aa5 , Prev_Value 5aaa , Rem Cost 1900 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 03cf  BS[1] 0c3f  BS[2] 3b16  BS[3] 5aaa , Prev_Value 38d9 , Rem Cost 1200 R

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 38d9  BS[1] 0c3f  BS[2] 3b16  BS[3] 5aaa , Prev_Value 14b7 , Rem Cost 1000 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 38d9  BS[1] 14b7  BS[2] 3b16  BS[3] 5aaa , Prev_Value 2fa1 , Rem Cost 300 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 38d9  BS[1] 14b7  BS[2] 2fa1  BS[3] 5aaa , Prev_Value eb48 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[2];
X[2] = F[1];
X[3] = F[3];

// to : 38D9 2FA1 EB48 5AAA 
// T-Depth : 4
// Depth : 39
