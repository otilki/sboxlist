// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[0];
F[2] = X[2];
F[3] = X[1];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] 3333  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 100

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 5555  BS[1] 00ff  BS[2] 3333  BS[3] a5a5 , Prev_Value f0f0 , Rem Cost 300

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 55f0  BS[1] 00ff  BS[2] 3333  BS[3] a5a5 , Prev_Value 5555 , Rem Cost 1000

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 55f0  BS[1] 00ff  BS[2] 66c3  BS[3] a5a5 , Prev_Value 3333 , Rem Cost 1200

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 55f0  BS[1] 00ff  BS[2] 66c3  BS[3] c366 , Prev_Value a5a5 , Rem Cost 1400

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 55f0  BS[1] 550f  BS[2] 66c3  BS[3] c366 , Prev_Value 00ff , Rem Cost 1600

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 14f6  BS[1] 550f  BS[2] 66c3  BS[3] c366 , Prev_Value 55f0 , Rem Cost 2300

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 14f6  BS[1] 550f  BS[2] 66c3  BS[3] c366 , Prev_Value 51cd , Rem Cost 2200 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 14f6  BS[1] 51cd  BS[2] 66c3  BS[3] c366 , Prev_Value 92ab , Rem Cost 1500 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 14f6  BS[1] 51cd  BS[2] 66c3  BS[3] 92ab , Prev_Value 7661 , Rem Cost 1300 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 14f6  BS[1] 51cd  BS[2] 7661  BS[3] 92ab , Prev_Value 453b , Rem Cost 600 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 453b  BS[1] 51cd  BS[2] 7661  BS[3] 92ab , Prev_Value 6d54 , Rem Cost 400 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 453b  BS[1] 51cd  BS[2] 7661  BS[3] 6d54 , Prev_Value 286f , Rem Cost 300 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 286f  BS[1] 51cd  BS[2] 7661  BS[3] 6d54 , Prev_Value 899e , Rem Cost 100 R


X[0] = F[3];
X[1] = F[2];
X[2] = F[1];
X[3] = F[0];

// to : 6D54 899E 51CD 286F 
// T-Depth : 4
// Depth : 41
