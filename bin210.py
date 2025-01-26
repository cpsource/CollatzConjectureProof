def binary_to_decimal(binary_str):
  """Converts a binary string to its decimal equivalent.

  Args:
    binary_str: The binary string to convert.

  Returns:
    The decimal equivalent of the binary string.
  """
  decimal = 0
  power = 0
  for digit in binary_str[::-1]:  # Iterate through digits in reverse
    decimal += int(digit) * 2**power
    power += 1
  return decimal

# Get binary string input from the user
binary_str = input("Enter a binary string: ")

# Convert to decimal and print the result
decimal_value = binary_to_decimal(binary_str)
print("The decimal equivalent is:", decimal_value)
