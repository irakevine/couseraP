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