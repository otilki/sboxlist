// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[1];
F[3] = X[2];

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 0f0f  BS[3] 3333 , Prev_Value 5555 , Rem Cost 100

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3c3c  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 300

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3c3c  BS[3] 1b1b , Prev_Value 3333 , Rem Cost 1000

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] c3c3  BS[3] 1b1b , Prev_Value 3c3c , Rem Cost 1100

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] c3d8  BS[3] 1b1b , Prev_Value c3c3 , Rem Cost 1800

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] c3d8  BS[3] d8c3 , Prev_Value 1b1b , Rem Cost 2000

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 887d  BS[1] aaaa  BS[2] c3d8  BS[3] d8c3 , Prev_Value 00ff , Rem Cost 2700

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 887d  BS[1] aaaa  BS[2] c3d8  BS[3] d8c3 , Prev_Value 2af2 , Rem Cost 2500 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 887d  BS[1] 2af2  BS[2] c3d8  BS[3] d8c3 , Prev_Value a28f , Rem Cost 1800 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 887d  BS[1] a28f  BS[2] c3d8  BS[3] d8c3 , Prev_Value 50be , Rem Cost 1600 R

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 50be  BS[1] a28f  BS[2] c3d8  BS[3] d8c3 , Prev_Value c356 , Rem Cost 1400 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 50be  BS[1] a28f  BS[2] c356  BS[3] d8c3 , Prev_Value 61d9 , Rem Cost 700 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 50be  BS[1] 61d9  BS[2] c356  BS[3] d8c3 , Prev_Value 273c , Rem Cost 500 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 50be  BS[1] 61d9  BS[2] c356  BS[3] 273c , Prev_Value 7782 , Rem Cost 400 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 7782  BS[1] 61d9  BS[2] c356  BS[3] 273c , Prev_Value b4d4 , Rem Cost 200 R


X[0] = F[0];
X[1] = F[2];
X[2] = F[1];
X[3] = F[3];

// to : 7782 B4D4 61D9 273C 
// T-Depth : 5
// Depth : 48
