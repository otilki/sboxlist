// from : 00FF 0F0F 3333 5555 

F[0] = X[0];
F[1] = X[1];
F[2] = X[2];
F[3] = X[3];

F[3] = CCNOT2(F[2], F[1], F[3]);
F[2] = CCNOT2(F[1], F[0], F[2]);
F[0] = CCNOT2(F[3], F[2], F[0]);
F[1] = CCNOT2(F[3], F[0], F[1]);

X[0] = F[2];
X[1] = F[3];
X[2] = F[0];
X[3] = F[1];

// to : 333C 5656 12EB 1D4D 
// T-Depth : 4
// Depth : 28
