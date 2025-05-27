// from : 00FF 0F0F 3333 5555 

F[0] = X[1];
F[1] = X[3];
F[2] = X[2];
F[3] = X[0];

F[1] = CCNOT2(F[3], F[0], F[1]);
Info_Op:  CCNOT, Info_Line: 1, Op_Values  BS[0] 0f0f  BS[1] 555a  BS[2] 3333  BS[3] 00ff , Prev_Value 5555 , Rem Cost 700

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] f0f0  BS[1] 555a  BS[2] 3333  BS[3] 00ff , Prev_Value 0f0f , Rem Cost 800

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] f0f0  BS[1] 555a  BS[2] cccc  BS[3] 00ff , Prev_Value 3333 , Rem Cost 900

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] f0f0  BS[1] 555a  BS[2] cccc  BS[3] ff00 , Prev_Value 00ff , Rem Cost 1000

F[0] = CCNOT2(F[3], F[2], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] cccc  BS[3] ff00 , Prev_Value f0f0 , Rem Cost 1700

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] cccc  BS[3] ff00 , Prev_Value d89c , Rem Cost 2100 R

F[3] = CCNOT2(F[2], F[1], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] d89c  BS[3] ff00 , Prev_Value af18 , Rem Cost 1400 R

F[3] = CNOT1(F[0], F[3]);
Info_Op:  CNOT, Info_Line: 3, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] d89c  BS[3] af18 , Prev_Value 93e8 , Rem Cost 700 R

F[2] = CNOT1(F[1], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] d89c  BS[3] 93e8 , Prev_Value 8dc6 , Rem Cost 500 R

F[2] = CNOT1(F[3], F[2]);
Info_Op:  CNOT, Info_Line: 2, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] 8dc6  BS[3] 93e8 , Prev_Value 1e2e , Rem Cost 300 R

F[1] = RNOT1(F[1]);
Info_Op:  RNOT, Info_Line: 1, Op_Values  BS[0] 3cf0  BS[1] 555a  BS[2] 1e2e  BS[3] 93e8 , Prev_Value aaa5 , Rem Cost 100 R


X[0] = F[0];
X[1] = F[1];
X[2] = F[3];
X[3] = F[2];

// to : 3CF0 AAA5 93E8 1E2E 
// T-Depth : 4
// Depth : 33
