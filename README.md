# CollatzConjectureProof
We prove the Collatz Conjecture

## What is the Collatz Conjecture?

From [wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture):

The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of integers in which each term is obtained from the previous term as follows: if a term is even, the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. The conjecture has been shown to hold for all positive integers up to 2.95×1020, but no general proof has been found. (Until now !)

## We use the binary numbering system

The proof relies on the **little-endian binary numbering system**, as suggested by the sequence of dividing by 2, which corresponds to a right shift in binary. In this system, the least significant bit (bit 0, representing ** 2^0 ** is on the far right and if set, the number is odd, followed by bit 1 ** (2^1) **, bit 2 ** 2^2 **, and so on.

## Note: Over the next week, I'll be publishing the proof here.
