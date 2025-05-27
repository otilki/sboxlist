// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[2];
F[2] = X[3];
F[3] = X[1];

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] 0f0f , Prev_Value 5555 , Rem Cost 100

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 0f0f , Rem Cost 200

F[0] = CCNOT2(F[2], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] aaaa  BS[3] f0f0 , Prev_Value 00ff , Rem Cost 900

F[2] = CNOT1(F[0], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0f0 , Prev_Value aaaa , Rem Cost 1100

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value f0f0 , Rem Cost 1800

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 22dd  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value 12fc , Rem Cost 1900 R

F[1] = CCNOT2(F[3], F[2], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] 3333  BS[2] 8877  BS[3] f0a5 , Prev_Value b316 , Rem Cost 1200 R

F[1] = CNOT1(F[0], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] b316  BS[2] 8877  BS[3] f0a5 , Prev_Value a1ea , Rem Cost 500 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 12fc  BS[1] a1ea  BS[2] 8877  BS[3] f0a5 , Prev_Value 7788 , Rem Cost 300 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 12fc  BS[1] a1ea  BS[2] 7788  BS[3] f0a5 , Prev_Value d662 , Rem Cost 200 R


X[0] = F[2];
X[1] = F[3];
X[2] = F[1];
X[3] = F[0];

// to : 7788 F0A5 D662 12FC 
// T-Depth : 4
// Depth : 35
