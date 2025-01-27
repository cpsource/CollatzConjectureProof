# CollatzConjectureProof
We prove the Collatz Conjecture

## What is the Collatz Conjecture?

From [wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture):

The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of integers in which each term is obtained from the previous term as follows: if a term is even, the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. The conjecture has been shown to hold for all positive integers up to 2.95×1020, but no general proof has been found. (Until now !)

## We use the binary numbering system

The proof relies on the **little-endian binary numbering system**, as suggested by the sequence of dividing by 2, which corresponds to a right shift in binary. In this system, the least significant bit (bit 0, representing 2<sup>0</sup> is on the far right and if set, the number is odd, followed by bit 1 2<sup>1</sup>, bit 2 2<sup>2</sup>, and so on.

## Here's the rule, part A and B we follow:

```
        if (not (accumulator & (1 << p_pstart))): # p_pstart = 0 typically
            # odd rule - part A - divide by 2
            accumulator >>= 1
        else:
            # even rule - part B - multiply by 3 then add 1
            accumulator = 3 * accumulator + (1 << p_pstart)

```

The accumulator is a 64 bit quantity we keep our number under test in.
<br>
p_pstart is always 0.

## Terminating condition

We can terminate our iterations if we only have one bit true remaining in
the accumulator. This is because the odd rule - Part A would continually
shift to the right until only bit 0 remained as true.

In binary mathematics, one shift to the right is the same as dividing by 2, and
a number is odd if bit 0 of the accumulator is a 1.

## Can we bound the accumulator in the next iteration?

Yes. If the accumulator is even, the resultant accumulator will have to
be 1/2 of the origional.

Yes for the odd case too. Starting out, the resultant accumulator will be 3
times the accumulator. However, since the '3' is odd, and we are multiplying
by an odd number, we will obtain an odd, but we add one to it to be even. This even
will result in the odd rule - Part A being invoked, which divides the result
by 2. We can write thi as:

```
  3/2
```
Or reduced to 1.5. So this means our resultant accumulator can't be more
than 1.5 times the origional accumulator.

Since we want to prove that for any N, we converge on 1, we need to get
this reduction factor below 1.

And we can.

## A new way to look at N

We can break N into two parts. The first being the first four bits, which we'll call
the track number. The remainder of N we can call N-upper. Thus

```
  N = N-upper + track-number
```

## Our rule can be viewed as a pseudo-random number generator

If the rule was purely random, track-number would be half even and half odd.

However, the rule is not truly random and therefore has a pattern.

Does this pattern help us further reduce our 3/2 ratio?

Yes.

## By experiment, track-number is shown to be even about 62% of the time.

You only need to run the experiment over all track-numbers and not N-upper.
You learn two things:
* That for every track-number, we converge to 1
* That track-number is even more than about 62% of the time

## Why don't I have to verify this for all N-upper.

This is because any multiply of N-upper will not effect the track-number. The
resultant number can not be lower than the initial N-upper.

## Can track-number change on rule Part B?

Yes, but it's still four bits, and therefore just becomes another track
number, that, because we've tested it, must also converge to 1.

## Back to our upper bound for the accumulator.

We had 3/2, but now I can also say tht 62% of the time, I will be dividing by
2. Our rule now becomes

```
  3/(2*2), or 3/4, or .75.
```

## Conclusion

Therefore, any N must converge to 1 over time. Therefore, we've proven the conjecture.








