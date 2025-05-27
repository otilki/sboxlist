// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[3];
F[3] = X[2];

F[3] = CCNOT2(F[2], F[0], F[3]);
Info_Op:  CCNOT, Info_Line: 3, Op_Values  BS[0] 00ff  BS[1] 0f0f  BS[2] 5555  BS[3] 3366 , Prev_Value 3333 , Rem Cost 700

F[0] = CCNOT2(F[3], F[1], F[0]);
Info_Op:  CCNOT, Info_Line: 0, Op_Values  BS[0] 03f9  BS[1] 0f0f  BS[2] 5555  BS[3] 3366 , Prev_Value 00ff , Rem Cost 1400

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] 03f9  BS[1] 0f0f  BS[2] 5555  BS[3] cc99 , Prev_Value 3366 , Rem Cost 1500

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] 03f9  BS[1] 0f0f  BS[2] aaaa  BS[3] cc99 , Prev_Value 5555 , Rem Cost 1600

F[2] = CCNOT2(F[1], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] 03f9  BS[1] 0f0f  BS[2] aaaa  BS[3] cc99 , Prev_Value a9a3 , Rem Cost 2100 R

F[1] = CNOT1(F[2], F[1]);
Info_Op:  CNOT, Info_Line: 1, Op_Values  BS[0] 03f9  BS[1] 0f0f  BS[2] a9a3  BS[3] cc99 , Prev_Value a6ac , Rem Cost 1400 R

F[0] = CNOT1(F[1], F[0]);
Info_Op:  CNOT, Info_Line: 0, Op_Values  BS[0] 03f9  BS[1] a6ac  BS[2] a9a3  BS[3] cc99 , Prev_Value a555 , Rem Cost 1200 R

F[2] = CCNOT2(F[3], F[0], F[2]);
Info_Op:  CCNOT, Info_Line: 2, Op_Values  BS[0] a555  BS[1] a6ac  BS[2] a9a3  BS[3] cc99 , Prev_Value 2db2 , Rem Cost 1000 R

F[2] = RNOT1(F[2]);
Info_Op:  RNOT, Info_Line: 2, Op_Values  BS[0] a555  BS[1] a6ac  BS[2] 2db2  BS[3] cc99 , Prev_Value d24d , Rem Cost 300 R

F[3] = RNOT1(F[3]);
Info_Op:  RNOT, Info_Line: 3, Op_Values  BS[0] a555  BS[1] a6ac  BS[2] d24d  BS[3] cc99 , Prev_Value 3366 , Rem Cost 200 R

F[0] = RNOT1(F[0]);
Info_Op:  RNOT, Info_Line: 0, Op_Values  BS[0] a555  BS[1] a6ac  BS[2] d24d  BS[3] 3366 , Prev_Value 5aaa , Rem Cost 100 R


X[0] = F[0];
X[1] = F[3];
X[2] = F[2];
X[3] = F[1];

// to : 5AAA 3366 D24D A6AC 
// T-Depth : 4
// Depth : 33
