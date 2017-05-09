def prime_number(number):
    """
    # A prime number is a number divisible by one or itself
    # Function to generate prime numbers within given range.
    """

    prime_nos = []

    if number in (0, 1):
        return "Zero or One cannot be prime numbers."

    if type(number) != int:
        return "Only integers are allowed."

    for i in range(2, number + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                prime_nos.append(i)
    return prime_nos


"""
# Call the function using an example of 20 to test whether is working
# Output:[2, 3, 5, 7, 11, 13, 17, 19]
"""
prime = prime_number(20)
print(prime)
