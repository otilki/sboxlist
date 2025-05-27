// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[0];
F[3] = X[2];

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 6666  BS[2] 00ff  BS[3] 3333 , Prev_Value 5555 , Rem Cost 200

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 6666  BS[2] 00ff  BS[3] cccc , Prev_Value 3333 , Rem Cost 300

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 6969  BS[2] 00ff  BS[3] cccc , Prev_Value 6666 , Rem Cost 500

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0fc3  BS[1] 6969  BS[2] 00ff  BS[3] cccc , Prev_Value 0f0f , Rem Cost 1200

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 0fc3  BS[1] 6969  BS[2] 6996  BS[3] cccc , Prev_Value 00ff , Rem Cost 1400

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0fc3  BS[1] 6969  BS[2] 6996  BS[3] c30f , Prev_Value cccc , Rem Cost 1600

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 6996  BS[3] c30f , Prev_Value 6969 , Rem Cost 2300

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 6996  BS[3] c30f , Prev_Value eb09 , Rem Cost 2200 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 0fc3  BS[1] 286f  BS[2] 6996  BS[3] eb09 , Prev_Value f03c , Rem Cost 1500 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] f03c  BS[1] 286f  BS[2] 6996  BS[3] eb09 , Prev_Value 899e , Rem Cost 1400 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] f03c  BS[1] 286f  BS[2] 899e  BS[3] eb09 , Prev_Value 79a2 , Rem Cost 700 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 79a2  BS[1] 286f  BS[2] 899e  BS[3] eb09 , Prev_Value 92ab , Rem Cost 500 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 79a2  BS[1] 286f  BS[2] 899e  BS[3] 92ab , Prev_Value 51cd , Rem Cost 300 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 51cd  BS[1] 286f  BS[2] 899e  BS[3] 92ab , Prev_Value 6d54 , Rem Cost 100 R


X[0] = F[3];
X[1] = F[2];
X[2] = F[0];
X[3] = F[1];

// to : 6D54 899E 51CD 286F 
// T-Depth : 4
// Depth : 40
