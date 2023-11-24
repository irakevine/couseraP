# Fill in the blanks to print the numbers 1 through 7.:"
# number = ___ # Initialize the variable
# while ___ # Complete the while loop condition
#     print(number, end=" ")
#     number ___ # Increment the variable

# # Should print 1 2 3 4 5 6 7 


# number = 1  # Initialize the variable
# while number <= 7:  # Complete the while loop condition
#     print(number, end=" ")
#     number += 1  # Increment the variable

# Question 3
# Fill in the blanks to complete the function “digits(n)” to count how many digits the given number has. For example: 25 has 2 digits and 144 has 3 digits. 

# Tip: you can count the digits of a number by dividing it by 10 once per digit until there are no digits left.:"
# def digits(n):
#     count = 0
#     if n == 0:
#         return 1  # 0 has 1 digit

#     while n != 0:  # Complete the while loop condition
#         n //= 10  # Divide the number by 10 to discard the rightmost digit
#         count += 1  # Increment the count for each digit
        
#     return count

# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1

def digits(n):
    count = 0
    if n == 0:
        return 1  # 0 has 1 digit

    while n != 0:  # Complete the while loop condition
        n //= 10  # Divide the number by 10 to discard the rightmost digit
        count += 1  # Increment the count for each digit
        
    return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1


# Question 4
# Fill in the blanks to complete the “sequence” function. This function should print a sequence of numbers in descending order, from the given "high" variable to the given "low" variable.  The range should make the loop run two times. Complete the range sequences in the nested loops so that the “sequence(1, 3)” function call prints the following:

# 3, 2, 1

# 3, 2, 1:"

# def sequence(low, high):
#     # Complete the outer loop range to make the loop run twice
#     # to create two rows
#     for x in range(___): 
#         # Complete the inner loop range to print the given variable
#         # numbers starting from "high" to "low" 
#         # Hint: To decrement a range parameter, use negative numbers
#         for y in range(___): 
#             if y == low:
#                 # Don’t print a comma after the last item
#                 print(str(y)) 
#             else:
#                 # Print a comma and a space between numbers
#                 print(str(y), end=", ") 

# sequence(1, 3)
# # Should print the sequence 3, 2, 1 two times, as shown above.
# "

def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low - 1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.


# Question 5
# Fill in the blanks to complete the “divisible” function. This function should count the number of values from 0 to the “max” parameter that are evenly divisible (no remainder) by the “divisor” parameter. Complete the code so that a function call like “divisible(100,10)” will return the number “10”.:"
# def divisible(max, divisor):
#     ___ # Initialize an incremental variable
#     for ___ # Complete the for loop
#         if x % divisor == 0:
#             ___ # Increment the appropriate variable
#     return count

# print(divisible(100, 10)) # Should be 10
# print(divisible(10, 3)) # Should be 4
# print(divisible(144, 17)) # Should be 9
# "

def divisible(max, divisor):
    count = 0  # Initialize an incremental variable
    for x in range(max + 1):  # Complete the for loop
        if x % divisor == 0:
            count += 1  # Increment the appropriate variable
    return count

print(divisible(100, 10))  # Should be 10
print(divisible(10, 3))    # Should be 4
print(divisible(144, 17))  # Should be 9
