// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[1];
F[2] = X[0];
F[3] = X[3];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 0f0f  BS[2] ff00  BS[3] 5555 , Prev_Value 00ff , Rem Cost 100

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] ff00  BS[3] 5555 , Prev_Value 0f0f , Rem Cost 300

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5a5a  BS[2] ff00  BS[3] aaaa , Prev_Value 5555 , Rem Cost 400

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] cc33  BS[1] 5a5a  BS[2] ff00  BS[3] aaaa , Prev_Value 3333 , Rem Cost 600

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] cc33  BS[1] 5a5a  BS[2] ff00  BS[3] f0aa , Prev_Value aaaa , Rem Cost 1300

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] cc33  BS[1] 9669  BS[2] ff00  BS[3] f0aa , Prev_Value 5a5a , Rem Cost 1500

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c99  BS[1] 9669  BS[2] ff00  BS[3] f0aa , Prev_Value cc33 , Rem Cost 1700

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3c99  BS[1] 9669  BS[2] eb09  BS[3] f0aa , Prev_Value ff00 , Rem Cost 2400

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c99  BS[1] 9669  BS[2] eb09  BS[3] f0aa , Prev_Value 7661 , Rem Cost 2100 R

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3c99  BS[1] 7661  BS[2] eb09  BS[3] f0aa , Prev_Value 92ab , Rem Cost 1400 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c99  BS[1] 7661  BS[2] eb09  BS[3] 92ab , Prev_Value d790 , Rem Cost 700 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3c99  BS[1] 7661  BS[2] d790  BS[3] 92ab , Prev_Value 899e , Rem Cost 500 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c99  BS[1] 899e  BS[2] d790  BS[3] 92ab , Prev_Value 286f , Rem Cost 400 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c99  BS[1] 899e  BS[2] 286f  BS[3] 92ab , Prev_Value 6d54 , Rem Cost 300 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c99  BS[1] 899e  BS[2] 286f  BS[3] 6d54 , Prev_Value 51cd , Rem Cost 200 R


X[0] = F[3];
X[1] = F[1];
X[2] = F[0];
X[3] = F[2];

// to : 6D54 899E 51CD 286F 
// T-Depth : 4
// Depth : 39
