// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[0];
F[3] = X[2];

F[0] = CNOT1(F[3], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 5555  BS[2] 00ff  BS[3] 3333 , Prev_Value 0f0f , Rem Cost 200

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 5555  BS[2] 00ff  BS[3] 33cc , Prev_Value 3333 , Rem Cost 400

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 00ff  BS[3] 33cc , Prev_Value 5555 , Rem Cost 1100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 00ff  BS[3] cc33 , Prev_Value 33cc , Rem Cost 1200

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] ff00  BS[3] cc33 , Prev_Value 00ff , Rem Cost 1300

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 9a59  BS[3] cc33 , Prev_Value ff00 , Rem Cost 1500

F[3] = CCCNOT2(F[0], F[1], F[2], F[3]);
Info_Op:  , Info_Line: 3, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 9a59  BS[3] cc2b , Prev_Value cc33 , Rem Cost 3600

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3c3c  BS[1] 6559  BS[2] 9a59  BS[3] cc2b , Prev_Value 3c65 , Rem Cost 2500 R

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] 6559  BS[2] 9a59  BS[3] cc2b , Prev_Value a972 , Rem Cost 1800 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] 6559  BS[2] 9a59  BS[3] a972 , Prev_Value ed09 , Rem Cost 1600 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 3c65  BS[1] ed09  BS[2] 9a59  BS[3] a972 , Prev_Value d16c , Rem Cost 900 R

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3c65  BS[1] d16c  BS[2] 9a59  BS[3] a972 , Prev_Value b916 , Rem Cost 700 R


X[0] = F[3];
X[1] = F[1];
X[2] = F[0];
X[3] = F[2];

// to : B916 D16C 3C65 9A59 
// T-Depth : 7
// Depth : 59
