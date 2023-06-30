# combinatorial_enumeration
This code calculates the number of DAGs (Directed Acyclic Graphs) on n labeled vertices and record them into a list.

The graph enumeration problem of counting directed acyclic graphs was studied by Robinson (1973). The number of DAGs on n labeled vertices, for n = 0, 1, 2, 3, … (without restrictions on the order in which these numbers appear in a topological ordering of the DAG) is

    1, 1, 3, 25, 543, 29281, 3781503, … (sequence A003024 in the OEIS).

These numbers may be computed by the recurrence relation 

![image](https://github.com/M3Rcrypt/combinatorial_enumeration/assets/88895789/610c5bed-a75f-4b72-b29c-3fb6ed9bd923)

Eric W. Weisstein conjectured, and McKay et al. (2004) proved, that the same numbers count the (0,1) matrices for which all eigenvalues are positive real numbers. The proof is bijective: a matrix A is an adjacency matrix of a DAG if and only if A + I is a (0,1) matrix with all eigenvalues positive, where I denotes the identity matrix. Because a DAG cannot have self-loops, its adjacency matrix must have a zero diagonal, so adding I preserves the property that all matrix coefficients are 0 or 1. (Wikipedia) 
