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

# I want this print this 
# print(divisible(100, 10))  # Should be 10
# print(divisible(10, 3))    # Should be 4
# print(divisible(144, 17))  # Should be 9
# :"
# 11
# 4
# 9



# def get_word(sentence, n):
    
#     if n > 0:
#         words = sentence.split()
#     the number of words
#         if n <= len(words):
#             return words[n - 1]  
#     return ""
# print(get_word("This is a lesson about lists", 4))  # Should print: lesson
# print(get_word("This is a lesson about lists", -4))  # Nothing

# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing



def get_word(sentence, n):
    if n > 0:
        words = sentence.split()
        if n <= len(words):
            return words[n - 1]
    return ""

print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing

print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing


# Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 


def file_size(file_info):
    _, _, size_in_bytes = file_info
    return "{:.2f}".format(size_in_bytes / 1024)

print(file_size(('Class Assignment', 'docx', 17875))) 
print(file_size(('Notes', 'txt', 496)))  
print(file_size(('Program', 'py', 1239)))  


# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.


def skip_elements(elements):
    return [element for index, element in enumerate(elements) if index % 2 == 0]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']



# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.


def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []


# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension. 
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename for filename in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    pig_latin_words = []
    for word in words:
        # Create the pig latin word and add it to the list
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    # Turn the list back into a phrase
    return " ".join(pig_latin_words)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.

def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}.".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])



# Want to give this a go? Fill in the blanks in the code to make it print a poem.

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = 'red'

violet = Flower()
violet.color = 'blue'

this_pun_is_for_you = "A little Python humor!"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)

# Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level.  The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote. 

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    # Exchange all apples between 'you' and 'me'
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    # Share and combine the total number of ideas
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

# We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"


class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table))  # Output: "This piece of furniture is made of brown wood"
print(describe_furniture(couch))  # Output: "This piece of furniture is made of red leather"



# Question 2
# Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level.  The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote.

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    # Exchange all apples between 'you' and 'me'
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    # Share and combine the total number of ideas
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# OK, now it’s your turn! Have a go at writing methods for a class.

# Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())  # Output: 21


# Want to see this in action?
 
#  In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.


class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f"hi, my name is {self.name}"

# Create a new instance with a name of your choice
some_person = Person("Alice")  
# Call the greeting method
print(some_person.greeting())


# Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, “Outputs a message with the name of the person”.

class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        """Outputs a message with the name of the person."""
        print("Hello! My name is {name}.".format(name=self.name))

help(Person.greeting)
