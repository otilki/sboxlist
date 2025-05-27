// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[0];
F[2] = X[2];
F[3] = X[3];

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 0f0f  BS[1] 00ff  BS[2] 3333  BS[3] aaaa , Prev_Value 5555 , Rem Cost 100

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 00ff  BS[2] 3333  BS[3] aaaa , Prev_Value 0f0f , Rem Cost 300

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0ff0  BS[1] 22dd  BS[2] 3333  BS[3] aaaa , Prev_Value 00ff , Rem Cost 1000

F[3] = CNOT1(F[1], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 0ff0  BS[1] 22dd  BS[2] 3333  BS[3] 8877 , Prev_Value aaaa , Rem Cost 1200

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 0ff0  BS[1] 22dd  BS[2] 3b43  BS[3] 8877 , Prev_Value 3333 , Rem Cost 1900

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 0ff0  BS[1] 22dd  BS[2] 3b43  BS[3] 8877 , Prev_Value 0fa5 , Rem Cost 2100 R

F[0] = CNOT1(F[2], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 0fa5  BS[1] 22dd  BS[2] 3b43  BS[3] 8877 , Prev_Value 34e6 , Rem Cost 1400 R

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 34e6  BS[1] 22dd  BS[2] 3b43  BS[3] 8877 , Prev_Value b835 , Rem Cost 1200 R

F[1] = CNOT1(F[3], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 34e6  BS[1] 22dd  BS[2] 3b43  BS[3] b835 , Prev_Value 9ae8 , Rem Cost 500 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] 34e6  BS[1] 9ae8  BS[2] 3b43  BS[3] b835 , Prev_Value cb19 , Rem Cost 300 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] cb19  BS[1] 9ae8  BS[2] 3b43  BS[3] b835 , Prev_Value 47ca , Rem Cost 200 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] cb19  BS[1] 9ae8  BS[2] 3b43  BS[3] 47ca , Prev_Value c4bc , Rem Cost 100 R


X[0] = F[2];
X[1] = F[0];
X[2] = F[3];
X[3] = F[1];

// to : C4BC CB19 47CA 9AE8 
// T-Depth : 4
// Depth : 37
