// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[2];
F[3] = X[1];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 5555  BS[2] 3333  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 100

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 55aa  BS[1] 5555  BS[2] 3333  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 300

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 55aa  BS[1] 5555  BS[2] 3333  BS[3] a55a , Prev_Value f0f0 , Rem Cost 500

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 44bb  BS[1] 5555  BS[2] 3333  BS[3] a55a , Prev_Value 55aa , Rem Cost 1200

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 44bb  BS[1] 5555  BS[2] 7722  BS[3] a55a , Prev_Value 3333 , Rem Cost 1900

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 44bb  BS[1] 514f  BS[2] 7722  BS[3] a55a , Prev_Value 5555 , Rem Cost 2600

F[0] = CCCNOT2(F[1], F[2], F[3], F[0]);
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 44bb  BS[1] 514f  BS[2] 7722  BS[3] a55a , Prev_Value 45b9 , Rem Cost 3900 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 45b9  BS[1] 514f  BS[2] 7722  BS[3] a55a , Prev_Value 266d , Rem Cost 1800 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 45b9  BS[1] 266d  BS[2] 7722  BS[3] a55a , Prev_Value e0e3 , Rem Cost 1600 R

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 45b9  BS[1] 266d  BS[2] 7722  BS[3] e0e3 , Prev_Value 65d8 , Rem Cost 1400 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 65d8  BS[1] 266d  BS[2] 7722  BS[3] e0e3 , Prev_Value 1f1c , Rem Cost 700 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 65d8  BS[1] 266d  BS[2] 7722  BS[3] 1f1c , Prev_Value 683e , Rem Cost 600 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 65d8  BS[1] 266d  BS[2] 683e  BS[3] 1f1c , Prev_Value 7ac4 , Rem Cost 400 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 65d8  BS[1] 266d  BS[2] 683e  BS[3] 7ac4 , Prev_Value 5ca9 , Rem Cost 200 R


X[0] = F[1];
X[1] = F[2];
X[2] = F[0];
X[3] = F[3];

// to : 266D 683E 65D8 5CA9 
// T-Depth : 7
// Depth : 62
