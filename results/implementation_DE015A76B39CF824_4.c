// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[0];
F[2] = X[2];
F[3] = X[1];

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] aaaa  BS[1] 00ff  BS[2] 3333  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] 00ff  BS[2] cccc  BS[3] 0f0f , Prev_Value 3333 , Rem Cost 200

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] 00ff  BS[2] cccc  BS[3] 0ff0 , Prev_Value 0f0f , Rem Cost 400

F[1] = CCNOT2(F[2], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] aaaa  BS[1] 8877  BS[2] cccc  BS[3] 0ff0 , Prev_Value 00ff , Rem Cost 1100

F[2] = CCNOT2(F[3], F[1], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] aaaa  BS[1] 8877  BS[2] c4bc  BS[3] 0ff0 , Prev_Value cccc , Rem Cost 1800

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] aaaa  BS[1] 8877  BS[2] c4bc  BS[3] f00f , Prev_Value 0ff0 , Rem Cost 1900

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] 8877  BS[2] c4bc  BS[3] f00f , Prev_Value aaaa , Rem Cost 2100

F[3] = CCNOT2(F[1], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 22dd  BS[1] 8877  BS[2] c4bc  BS[3] f00f , Prev_Value f05a , Rem Cost 2100 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 22dd  BS[1] 8877  BS[2] c4bc  BS[3] f05a , Prev_Value 3b43 , Rem Cost 1400 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 22dd  BS[1] 8877  BS[2] 3b43  BS[3] f05a , Prev_Value b835 , Rem Cost 1300 R

F[3] = CNOT1(F[2], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 22dd  BS[1] b835  BS[2] 3b43  BS[3] f05a , Prev_Value cb19 , Rem Cost 600 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] b835  BS[2] 3b43  BS[3] cb19 , Prev_Value 9ae8 , Rem Cost 400 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 9ae8  BS[1] b835  BS[2] 3b43  BS[3] cb19 , Prev_Value 47ca , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 9ae8  BS[1] 47ca  BS[2] 3b43  BS[3] cb19 , Prev_Value c4bc , Rem Cost 100 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[1];
X[3] = F[0];

// to : C4BC CB19 47CA 9AE8 
// T-Depth : 4
// Depth : 35
