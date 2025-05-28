// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[1];
F[3] = X[2];

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 5566  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 700

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5566  BS[2] 0f0f  BS[3] cccc , Prev_Value 3333 , Rem Cost 800

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 5566  BS[2] 0f0f  BS[3] cccc , Prev_Value 00ff , Rem Cost 1000

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0ff0  BS[1] 5566  BS[2] c3c3  BS[3] cccc , Prev_Value 0f0f , Rem Cost 1200

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 4bb4  BS[1] 5566  BS[2] c3c3  BS[3] cccc , Prev_Value 0ff0 , Rem Cost 1900

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 5566  BS[2] c3c3  BS[3] cccc , Prev_Value 8f4c , Rem Cost 2000 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 4bb4  BS[1] 5566  BS[2] c3c3  BS[3] 8f4c , Prev_Value 96a5 , Rem Cost 1300 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] c3c3  BS[3] 8f4c , Prev_Value 19e9 , Rem Cost 1100 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] c3c3  BS[3] 19e9 , Prev_Value ca63 , Rem Cost 900 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] ca63  BS[3] 19e9 , Prev_Value 359c , Rem Cost 200 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 4bb4  BS[1] 96a5  BS[2] 359c  BS[3] 19e9 , Prev_Value e616 , Rem Cost 100 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[1];
X[3] = F[0];

// to : 359C E616 96A5 4BB4 
// T-Depth : 4
// Depth : 37
