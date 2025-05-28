// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[3];
F[2] = X[2];
F[3] = X[1];

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] 3333  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] cccc  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 200

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] aaaa  BS[2] cccc  BS[3] c3c3 , Prev_Value 0f0f , Rem Cost 400

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6a6a  BS[2] cccc  BS[3] c3c3 , Prev_Value aaaa , Rem Cost 1100

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 6a6a  BS[2] a6a6  BS[3] c3c3 , Prev_Value cccc , Rem Cost 1300

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 6a6a  BS[2] a6a6  BS[3] c33c , Prev_Value c3c3 , Rem Cost 1500

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 6a56  BS[2] a6a6  BS[3] c33c , Prev_Value 6a6a , Rem Cost 2200

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 6a56  BS[2] a6a6  BS[3] c33c , Prev_Value 22f9 , Rem Cost 2000 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 22f9  BS[1] 6a56  BS[2] a6a6  BS[3] c33c , Prev_Value 659a , Rem Cost 1300 R

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 22f9  BS[1] 6a56  BS[2] 659a  BS[3] c33c , Prev_Value e16c , Rem Cost 1100 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 22f9  BS[1] 6a56  BS[2] 659a  BS[3] e16c , Prev_Value c395 , Rem Cost 400 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] c395  BS[1] 6a56  BS[2] 659a  BS[3] e16c , Prev_Value a9c3 , Rem Cost 200 R


X[0] = F[3];
X[1] = F[0];
X[2] = F[1];
X[3] = F[2];

// to : E16C C395 A9C3 659A 
// T-Depth : 4
// Depth : 39
