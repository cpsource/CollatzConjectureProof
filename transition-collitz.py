
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

# track transitions from say 5->11, etc
transitions_array = [0] * 256

def collatz(acc_start, p_pstart, flag):
    """
    This function implements the Collatz conjecture.

    Args:
      acc_start: The starting value for the accumulator.
      p_pstart:  (Unused in this implementation)
      flag:      If True, prints the loop count and accumulator in binary.
    """
    global transitions_array
    
    accumulator = acc_start << p_pstart
    loop_count = 0

    ctr_cnt = 0
    ctr_array = [0] * 16

    if ( flag ) :
      # keep track of occurences of low 4 bits
      print(f"\n{'cnt':>4s} {'binary accumulator (acc)':>64s} {'acc':>4s} {'bits':>4s}")
      print("-" * (4 + 64 + 4 + 4 + 3))  # 3 spaces for the gaps between columns
      #ctr_cnt += 1
      #ctr_array [ 0xf & accumulator ] += 1
      print(f"{loop_count:04d}", format(accumulator, '064b'), format(accumulator,'04d'), count_ones(accumulator))

    while True:

        transition_start = accumulator
        
        if (not (accumulator & (1 << p_pstart))): # p_pstart = 0 typically
            # odd rule - part A - divide by 2
            accumulator >>= 1
        else:
            # even rule - part B - multiply by 3 then add 1
            accumulator = 3 * accumulator + (1 << p_pstart)

        transition_end = accumulator
        
        # keep track of occurences of low 4 bits
        ctr_cnt += 1
        ctr_array [ 0xf & accumulator ] += 1

        # keep track of transitions
        idx = (transition_start & 0xf) + (transition_end & 0xf)*16
        #print(idx)
        transitions_array [ idx ] += 1

        if ( flag ) :
            #b3 = display_base3(accumulator)
            b3 = accumulator & 0xf
            loop_count += 1
            print(f"{loop_count:04d}", format(accumulator, '064b'), format(accumulator,'10d'), format(count_ones(accumulator),'3d'), format(b3,'02d'))

        # Terminating condition ???
        if count_ones(accumulator) == 1:
            break

    if ( flag ) :
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

    global transitions_array
    
    for i in range(16):  # Loop from 0 to 15
      print(f"Outer loop i: {i}")
      for j in range(16):  # Example: Loop j from 0 to 15
        print(f"  Inner loop j: {j}")

        a = i + j * 16
        if count_ones(a) > 1 :
          collatz(a, 0, 0)

    collatz(5649499, 0, 0)
    
    print(transitions_array)
    if False :
        # Display each value with its index
        for index, value in enumerate(transitions_array):
            print(f"Index: {index}, Value: {value}")
    
    # create probability array
    s = sum(transitions_array)
    f_array = [element / s for element in transitions_array]

    # Format the output as a list with four decimal places for each element
    f_output = "[" + ", ".join(f"{prob:.4f}" for prob in f_array) + f"]\n"
    # Print the formatted output
    print("Probability array",f_output)

    # Calculate the sum of elements at indices 0, 2, 4, ... E (14)
    sum_of_elements = sum(f_array[i] for i in range(0, len(f_array), 2))
    #print(sum_of_elements)
    # Format the number as a percentage with one decimal place
    formatted_percentage = "{:.1%}".format(sum_of_elements)
    # Print the formatted percentage
    print("Percentage of time we'll draw bit 0 as zero",formatted_percentage, f"\n")
          
if __name__ == "__main__":
    main()
