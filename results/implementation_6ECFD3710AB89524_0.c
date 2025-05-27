// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[2];
F[3] = X[0];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] cccc  BS[3] 00ff , Prev_Value 3333 , Rem Cost 100

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 5555  BS[2] cccc  BS[3] 05fa , Prev_Value 00ff , Rem Cost 800

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 50af  BS[2] cccc  BS[3] 05fa , Prev_Value 5555 , Rem Cost 1000

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 50af  BS[2] cccc  BS[3] fa05 , Prev_Value 05fa , Rem Cost 1100

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 98ab  BS[2] cccc  BS[3] fa05 , Prev_Value 50af , Rem Cost 1800

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0f0f  BS[1] 98ab  BS[2] cccc  BS[3] fa05 , Prev_Value 8787 , Rem Cost 1900 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 8787  BS[1] 98ab  BS[2] cccc  BS[3] fa05 , Prev_Value 4ec9 , Rem Cost 1200 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 8787  BS[1] 98ab  BS[2] 4ec9  BS[3] fa05 , Prev_Value d662 , Rem Cost 500 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 8787  BS[1] 98ab  BS[2] d662  BS[3] fa05 , Prev_Value 1f2c , Rem Cost 300 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 8787  BS[1] 1f2c  BS[2] d662  BS[3] fa05 , Prev_Value 7878 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[2];
X[3] = F[1];

// to : 7878 FA05 D662 1F2C 
// T-Depth : 4
// Depth : 36
