// from : 00FF 0F0F 3333 5555 

F[0] = X[3];
F[1] = X[2];
F[2] = X[1];
F[3] = X[0];

F[0] = RNOT1(F[0]);
F[3] = RNOT1(F[3]);
F[2] = RNOT1(F[2]);
F[0] = CCNOT2(F[3], F[2], F[0]);
F[1] = CCNOT2(F[3], F[0], F[1]);
F[2] = CCNOT2(F[1], F[0], F[2]);
F[3] = CCNOT2(F[2], F[1], F[3]);
F[0] = RNOT1(F[0]);
F[2] = RNOT1(F[2]);
F[3] = RNOT1(F[3]);
F[1] = RNOT1(F[1]);

X[0] = F[2];
X[1] = F[1];
X[2] = F[0];
X[3] = F[3];

// to : 472D 96CC A555 28ED 
// T-Depth : 4
// Depth : 30
