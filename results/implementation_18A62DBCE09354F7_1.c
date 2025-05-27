// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[2];
F[2] = X[3];
F[3] = X[0];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] aaaa  BS[3] 00ff , Prev_Value 5555 , Rem Cost 100

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] aaaa  BS[3] 0ff0 , Prev_Value 00ff , Rem Cost 300

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0f0f  BS[1] 3333  BS[2] a9a9  BS[3] 0ff0 , Prev_Value aaaa , Rem Cost 1000

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 3a93  BS[2] a9a9  BS[3] 0ff0 , Prev_Value 3333 , Rem Cost 1700

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 3a93  BS[2] a9a9  BS[3] f00f , Prev_Value 0ff0 , Rem Cost 1800

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 359c  BS[1] 3a93  BS[2] a9a9  BS[3] f00f , Prev_Value 0f0f , Rem Cost 2000

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 359c  BS[1] 3a93  BS[2] a9a9  BS[3] d187 , Prev_Value f00f , Rem Cost 2700

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 359c  BS[1] 3a93  BS[2] a9a9  BS[3] d187 , Prev_Value b92a , Rem Cost 2700 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 359c  BS[1] 3a93  BS[2] b92a  BS[3] d187 , Prev_Value 83b9 , Rem Cost 2000 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 359c  BS[1] 3a93  BS[2] 83b9  BS[3] d187 , Prev_Value e41b , Rem Cost 1800 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 359c  BS[1] 3a93  BS[2] 83b9  BS[3] e41b , Prev_Value 158f , Rem Cost 1600 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 158f  BS[1] 3a93  BS[2] 83b9  BS[3] e41b , Prev_Value 67a2 , Rem Cost 900 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 158f  BS[1] 3a93  BS[2] 83b9  BS[3] 67a2 , Prev_Value 863b , Rem Cost 700 R


X[0] = F[3];
X[1] = F[0];
X[2] = F[1];
X[3] = F[2];

// to : 67A2 158F 3A93 863B 
// T-Depth : 6
// Depth : 50
