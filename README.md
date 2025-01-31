CollatzConjectureProof

We prove the Collatz Conjecture

## What is the Collatz Conjecture?

From [wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture):

The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of integers in which each term is obtained from the previous term as follows: if a term is even, the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. The conjecture has been shown to hold for all positive integers up to 2.95×1020, but no general proof has been found. (Until now !)

## Note: deepseek dialog

I tried out the LLM deepseek to see how well it worked on a difficult and unknown problem. The results can be read [here](https://github.com/cpsource/CollatzConjectureProof/blob/main/collatz-deepseek-flow.md)
It didn't think much of the proof I presented. As for a LLM, at a certain point, it starting hanging and couldn't answer my quesions. I got the feeling it couldn't go where no one had gone before. The model was fine with the known, but as soon as I pushed it, it was out of its league.

## Note: switching to Chatgpt 4o

Next, I pushed this LLM into the unknown and came up with what it thinks is a proof of the conjecture. For any N, it shows that
the bit sequences must converge to ....010101.... and therefore eventually reduce to one. The discussion with ChatGpt 4o can be found [here]().

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
* That we never get the same state twice on any given track

## Why don't I have to verify this for all N-upper.

This is because any multiply of N-upper will not effect the track-number. The
resultant number can not be lower than the initial N-upper.

## Can track-number change on rule Part B?

Yes, but it's still four bits, and therefore just becomes another track
number, that, because we've tested it, must also converge to 1.

## Back to our upper bound for the accumulator.

We had 3/2, but now I can also say that 62% of the time, I will be dividing by
2. Our rule now becomes

```
  3/(2*2), or 3/4, or .75.
```

## Conclusion

Therefore, any N must converge to 1 over time. Therefore, we've proven the conjecture.

## c1-collatz.py

Included with this proof is the c1-collatz.py python program. It displays each iteration until
termination.

To run it:

```
  python3 c1-collatz.py N 0 0

```

You might try number 5649499 as it iterates 608 times before conclusion.

## We rely on house odds to converge, but iterations don't always.

As you watch the printout, notice that we get runs where our accumulator
increases. We would expect this, as 38% of the time, the accumulator will
increase by 1.5 times.

These runs don't last as the house always has the odds, and the
accumulator will begin to decrease again, eventually reaching 1.

Further, 10^20 N's have been tested and converge to 1. This certainly
tests every state transition in every track, without seeing an infinite loop
remaining withn the 38%.

You can run ./loop256.sh to loop through all possible combinations of track-number for all necessary N
to show that they all converge to 1 and that all permutations of bits 2<sup>7</sup> through 2<sup>0</sup>
have a convergent property greater than 60%.

