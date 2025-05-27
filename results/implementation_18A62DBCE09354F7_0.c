// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[2];
F[3] = X[3];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3333  BS[3] aaaa , Prev_Value 5555 , Rem Cost 100

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 0f0f  BS[2] 3333  BS[3] aaaa , Prev_Value 00ff , Rem Cost 300

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0ff0  BS[1] 0f0f  BS[2] 3333  BS[3] a9a9 , Prev_Value aaaa , Rem Cost 1000

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0ff0  BS[1] 0f0f  BS[2] 3a93  BS[3] a9a9 , Prev_Value 3333 , Rem Cost 1700

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0ff0  BS[1] 359c  BS[2] 3a93  BS[3] a9a9 , Prev_Value 0f0f , Rem Cost 1900

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2e78  BS[1] 359c  BS[2] 3a93  BS[3] a9a9 , Prev_Value 0ff0 , Rem Cost 2600

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 2e78  BS[1] 359c  BS[2] 3a93  BS[3] a9a9 , Prev_Value 83b9 , Rem Cost 2600 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 2e78  BS[1] 359c  BS[2] 3a93  BS[3] 83b9 , Prev_Value 1be4 , Rem Cost 1900 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 1be4  BS[1] 359c  BS[2] 3a93  BS[3] 83b9 , Prev_Value e41b , Rem Cost 1700 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] e41b  BS[1] 359c  BS[2] 3a93  BS[3] 83b9 , Prev_Value 158f , Rem Cost 1600 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] e41b  BS[1] 158f  BS[2] 3a93  BS[3] 83b9 , Prev_Value 67a2 , Rem Cost 900 R

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 67a2  BS[1] 158f  BS[2] 3a93  BS[3] 83b9 , Prev_Value 863b , Rem Cost 700 R


X[0] = F[0];
X[1] = F[1];
X[2] = F[2];
X[3] = F[3];

// to : 67A2 158F 3A93 863B 
// T-Depth : 6
// Depth : 51
