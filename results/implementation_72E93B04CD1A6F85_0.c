// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 3366 , Prev_Value 3333 , Rem Cost 700

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 3c69  BS[2] 5555  BS[3] 3366 , Prev_Value 0f0f , Rem Cost 900

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c69  BS[2] 5555  BS[3] cc99 , Prev_Value 3366 , Rem Cost 1000

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c96  BS[1] 3c69  BS[2] 5555  BS[3] cc99 , Prev_Value 00ff , Rem Cost 1200

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c96  BS[1] 3c69  BS[2] 5555  BS[3] 99cc , Prev_Value cc99 , Rem Cost 1400

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c96  BS[1] 3c69  BS[2] 69c3  BS[3] 99cc , Prev_Value 5555 , Rem Cost 1600

F[0] = CCCNOT2(F[1], F[2], F[3], F[0]);
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 34d6  BS[1] 3c69  BS[2] 69c3  BS[3] 99cc , Prev_Value 3c96 , Rem Cost 3700

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 34d6  BS[1] 3c69  BS[2] 69c3  BS[3] 99cc , Prev_Value 7907 , Rem Cost 2500 R

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 34d6  BS[1] 3c69  BS[2] 7907  BS[3] 99cc , Prev_Value a1cd , Rem Cost 1800 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 34d6  BS[1] 3c69  BS[2] 7907  BS[3] a1cd , Prev_Value 4dd1 , Rem Cost 1100 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 34d6  BS[1] 3c69  BS[2] 4dd1  BS[3] a1cd , Prev_Value ec1c , Rem Cost 900 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 34d6  BS[1] 3c69  BS[2] ec1c  BS[3] a1cd , Prev_Value 9c65 , Rem Cost 700 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[2];
X[3] = F[1];

// to : 34D6 A1CD EC1C 9C65 
// T-Depth : 7
// Depth : 60
