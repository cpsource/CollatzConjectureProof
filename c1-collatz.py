def display_base3(num):
  """Displays an integer as a base-3 string.

  Args:
    num: The integer to convert to base-3.
  """

  if num == 0:
    print("0")
    return

  base3_str = ""
  while num > 0:
    remainder = num % 3
    base3_str = str(remainder) + base3_str
    num //= 3

  return base3_str

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

    ctr_cnt = 0
    ctr_array = [0] * 16

    # keep track of occurences of low 4 bits
    print(f"\n{'cnt':>4s} {'binary accumulator (acc)':>64s} {'acc':>4s} {'bits':>4s}")
    print("-" * (4 + 64 + 4 + 4 + 3))  # 3 spaces for the gaps between columns
    #ctr_cnt += 1
    #ctr_array [ 0xf & accumulator ] += 1

    print(f"{loop_count:04d}", format(accumulator, '064b'), format(accumulator,'04d'), count_ones(accumulator))
    while True:
        if (not (accumulator & (1 << p_pstart))): # p_pstart = 0 typically
            # odd rule - part A - divide by 2
            accumulator >>= 1
        else:
            # even rule - part B - multiply by 3 then add 1
            accumulator = 3 * accumulator + (1 << p_pstart)

        # keep track of occurences of low 4 bits
        ctr_cnt += 1
        ctr_array [ 0xf & accumulator ] += 1

        #b3 = display_base3(accumulator)
        b3 = accumulator & 0xf
        loop_count += 1
        print(f"{loop_count:04d}", format(accumulator, '064b'), format(accumulator,'10d'), format(count_ones(accumulator),'3d'), format(b3,'02d'))

        # Terminating condition ???
        if count_ones(accumulator) == 1:
            break

    print (f"\n")
    
    # display ctr_array
    #print(f"ctr_cnt = {ctr_cnt}")
    #print(ctr_array)
    # create probability array
    float_array = [element / ctr_cnt for element in ctr_array]

    # Format the output as a list with four decimal places for each element
    formatted_output = "[" + ", ".join(f"{prob:.4f}" for prob in float_array) + f"]\n"
    # Print the formatted output
    print("Probability array",formatted_output)

    # Calculate the sum of elements at indices 0, 2, 4, ... E (14)
    sum_of_elements = sum(float_array[i] for i in range(0, len(float_array), 2))
    #print(sum_of_elements)
    # Format the number as a percentage with one decimal place
    formatted_percentage = "{:.1%}".format(sum_of_elements)
    # Print the formatted percentage
    print("Percentage of time we'll draw bit 0 as zero",formatted_percentage, f"\n")
    
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

    if count_ones(acc_start) > 1:
      collatz(acc_start, p_pstart, flag)

if __name__ == "__main__":
    main()
