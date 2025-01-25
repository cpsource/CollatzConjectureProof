def count_ones(n):
    """
    Counts the number of 1 bits in the binary representation of an integer.

    Args:
      n: The integer to count the 1 bits in.

    Returns:
      The number of 1 bits in the binary representation of n.
    """
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count

def collatz(acc_start, p_pstart, flag):
    """
    This function implements the Collatz conjecture.

    Args:
      acc_start: The starting value for the accumulator.
      p_pstart:  (Unused in this implementation)
      flag:      If True, prints the loop count and accumulator in binary.
    """
    accumulator = acc_start << p_pstart
    loop_count = 0
    while True:
        if ( flag ) :
            print(f"{loop_count:04d}", format(accumulator, '064b'), format(accumulator,'04d'), count_ones(accumulator))
        if (not (accumulator & (1 << p_pstart))):
            accumulator >>= 1
        else:
            accumulator = 3 * accumulator + (1 << p_pstart)
        loop_count += 1
        if count_ones(accumulator) == 1:
            if ( flag ) :
                print(f"{loop_count:04d}", format(accumulator, '064b'), format(accumulator,'04d'), count_ones(accumulator))
            break
    return loop_count

def main():
    """
    Parses command line arguments and calls the collatz function.
    """
    import sys
    if len(sys.argv) != 4:
        print("Usage: python collatz.py <acc_start> <p_pstart> <flag>")
        sys.exit(1)

    acc_start = int(sys.argv[1])
    p_pstart = int(sys.argv[2])  # Currently unused
    flag = bool(int(sys.argv[3]))  # Convert string to boolean

    largest = 1
    largest_number = 1

    for i in range (acc_start, 10000000):
        tmp_size = collatz(i, p_pstart, 0)
        if ( tmp_size > largest ) :
            largest = tmp_size
            largest_number = i
            print(f"largest: largest = {largest}, largest_number = {largest_number}")            

    print(f"largest: largest = {largest}, largest_number = {largest_number}")
    
if __name__ == "__main__":
    main()
