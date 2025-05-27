// from : 00FF 0F0F 3333 5555 

F[0] = X[2];
F[1] = X[3];
F[2] = X[1];
F[3] = X[0];

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 0ff0  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 200

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 5aa5  BS[3] 00ff , Prev_Value 0ff0 , Rem Cost 400

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3333  BS[1] 5555  BS[2] 5aa5  BS[3] 33cc , Prev_Value 00ff , Rem Cost 600

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2277  BS[1] 5555  BS[2] 5aa5  BS[3] 33cc , Prev_Value 3333 , Rem Cost 1300

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2277  BS[1] 7722  BS[2] 5aa5  BS[3] 33cc , Prev_Value 5555 , Rem Cost 1500

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 2277  BS[1] 7722  BS[2] 5aa5  BS[3] 6969 , Prev_Value 33cc , Rem Cost 1700

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 2277  BS[1] 5743  BS[2] 5aa5  BS[3] 6969 , Prev_Value 7722 , Rem Cost 2400

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 2277  BS[1] 5743  BS[2] 5aa5  BS[3] 6969 , Prev_Value 3b68 , Rem Cost 2700 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 2277  BS[1] 5743  BS[2] 5aa5  BS[3] 3b68 , Prev_Value c497 , Rem Cost 2000 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 2277  BS[1] 5743  BS[2] 5aa5  BS[3] c497 , Prev_Value 9e32 , Rem Cost 1900 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 2277  BS[1] 5743  BS[2] 9e32  BS[3] c497 , Prev_Value c971 , Rem Cost 1700 R

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 2277  BS[1] c971  BS[2] 9e32  BS[3] c497 , Prev_Value 9e43 , Rem Cost 1500 R

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 2277  BS[1] c971  BS[2] 9e43  BS[3] c497 , Prev_Value a674 , Rem Cost 800 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] a674  BS[1] c971  BS[2] 9e43  BS[3] c497 , Prev_Value 368e , Rem Cost 100 R


X[0] = F[1];
X[1] = F[3];
X[2] = F[0];
X[3] = F[2];

// to : 368E C497 A674 9E43 
// T-Depth : 5
// Depth : 46
