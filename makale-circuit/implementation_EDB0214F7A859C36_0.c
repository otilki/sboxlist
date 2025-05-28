// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 6666  BS[3] 3333 , Prev_Value 5555 , Rem Cost 200

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6666  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 400

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6666  BS[3] cccc , Prev_Value 3333 , Rem Cost 500

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6666  BS[3] cc33 , Prev_Value cccc , Rem Cost 700

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3c3c  BS[2] 6a56  BS[3] cc33 , Prev_Value 6666 , Rem Cost 1400

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 3c6a  BS[2] 6a56  BS[3] cc33 , Prev_Value 3c3c , Rem Cost 2100

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3c6a  BS[2] 6a56  BS[3] cc33 , Prev_Value cc59 , Rem Cost 2100 R

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 3c6a  BS[2] 6a56  BS[3] cc59 , Prev_Value 48af , Rem Cost 1400 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 48af  BS[1] 3c6a  BS[2] 6a56  BS[3] cc59 , Prev_Value c395 , Rem Cost 700 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 48af  BS[1] c395  BS[2] 6a56  BS[3] cc59 , Prev_Value a9c3 , Rem Cost 600 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 48af  BS[1] c395  BS[2] a9c3  BS[3] cc59 , Prev_Value 659a , Rem Cost 400 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 48af  BS[1] c395  BS[2] a9c3  BS[3] 659a , Prev_Value e16c , Rem Cost 200 R


X[0] = F[0];
X[1] = F[1];
X[2] = F[2];
X[3] = F[3];

// to : E16C C395 A9C3 659A 
// T-Depth : 4
// Depth : 41
