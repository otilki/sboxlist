// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[0];
F[3] = X[1];

F[3] = RNOT1(F[3]);
F[2] = RNOT1(F[2]);
F[2] = CCNOT2(F[3], F[0], F[2]);
F[3] = CNOT1(F[1], F[3]);
F[1] = CNOT1(F[2], F[1]);
F[3] = CCNOT2(F[2], F[0], F[3]);
F[0] = CCNOT2(F[3], F[1], F[0]);
F[2] = CNOT1(F[3], F[2]);
F[0] = CNOT1(F[2], F[0]);
F[3] = RNOT1(F[3]);
F[1] = CCNOT2(F[3], F[0], F[1]);

X[0] = F[0];
X[1] = F[2];
X[2] = F[3];
X[3] = F[1];

// to : B895 69C3 396C A467 
// T-Depth : 4
// Depth : 37
