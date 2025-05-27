// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[2];
F[3] = X[3];

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3333  BS[3] 5656 , Prev_Value 5555 , Rem Cost 700

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3c3c  BS[3] 5656 , Prev_Value 3333 , Rem Cost 900

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 3cc3  BS[3] 5656 , Prev_Value 3c3c , Rem Cost 1100

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 00ff  BS[1] 1b4d  BS[2] 3cc3  BS[3] 5656 , Prev_Value 0f0f , Rem Cost 1800

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 1b4d  BS[2] 3c8e  BS[3] 5656 , Prev_Value 3cc3 , Rem Cost 2500

F[0] = CCCNOT2(F[1], F[2], F[3], F[0]);
Info_Op:  , Info_Line: 0, Op_Values  BS[0] 00ff  BS[1] 1b4d  BS[2] 3c8e  BS[3] 5656 , Prev_Value 10fb , Rem Cost 3700 R

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 10fb  BS[1] 1b4d  BS[2] 3c8e  BS[3] 5656 , Prev_Value 2c75 , Rem Cost 1600 R

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 10fb  BS[1] 1b4d  BS[2] 2c75  BS[3] 5656 , Prev_Value 46ad , Rem Cost 1400 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 46ad  BS[1] 1b4d  BS[2] 2c75  BS[3] 5656 , Prev_Value 3738 , Rem Cost 1200 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 46ad  BS[1] 3738  BS[2] 2c75  BS[3] 5656 , Prev_Value c8c7 , Rem Cost 1000 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 46ad  BS[1] c8c7  BS[2] 2c75  BS[3] 5656 , Prev_Value 9e91 , Rem Cost 900 R

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 46ad  BS[1] c8c7  BS[2] 2c75  BS[3] 9e91 , Prev_Value cce2 , Rem Cost 700 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[1];
X[3] = F[2];

// to : 46AD 9E91 CCE2 2C75 
// T-Depth : 7
// Depth : 60
