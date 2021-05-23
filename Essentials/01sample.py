######################### GENERALS IN MSFT ##################################
# print("Hello world")
# x = 1
# y = 16.1
# z = True
# a= 'this is a string'+ ' nowhere is safe'
# b= "Also this is string"+ " wow great"
# print(b)

# name = input('Enter NAME:')
# print('Your name is : ' + name) 

# age = int(input('Enter age:'))
# print(type(age)) 
# print("Your age is " + str(age))
######################## INPUTS ####################################

# print('welcome')
# name = input('enter your name :')
# print('hello '+ name)

######################### NUMBERS ##################################

# myfloat = 7.0
# print(myfloat)
# myfloat = float(7)
# print(myfloat)

######################### STRINGS ##################################

# mystring = 'hello'
# print(mystring)

# mystring = "hello cbg"
# print(mystring)

# mystring = " don't worry about apostrophes"
# print(mystring)

# one = 1
# two = 2
# three = one + two
# print(three)

# hello = "hello"
# world = "world"
# helloworld = hello + " " + world
# print(helloworld)

# a, b = 3, 4
# print(a,b)

# # This will not work !Mixing operators between numbers and strings is not supported:
# one = 1
# two = 2
# hello = "hello"

##print(int(one) + int(two) + hello)
######################### LISTS ##################################

# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# print(mylist[0]) # prints 1
# print(mylist[1]) # prints 2
# print(mylist[2]) # prints 3

# # prints out 1,2,3
# for x in mylist:
#     print(x)

# Exercise
# numbers = []
# strings = []
# names = ["John" , "Eric" , "Jessica"]

# numbers.append(1)
# numbers.append(2)
# numbers.append(3)

# strings.append("hello")
# strings.append("world")
# second_name = names[1]

# print(numbers)
# print(strings)
# print("Second name on the names list is %s" %second_name)

######################### BASIC OPERATORS ##################################
# #ARITHMETIC Ops
# number = 1 + 2 * 3 / 4.0
# print(number) 

# remainder = 11 % 3
# print(remainder)

# squared = 7 ** 2
# cubed = 2 ** 3
# print(squared)
# print(cubed)

# #Operators with Strings
# helloworld = "hello" + " " + "world"
# print(helloworld)

# lotsofhellos = "hello " * 10
# print(lotsofhellos)

# #Operators with Lists -- can be joined with the addition operators
# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]

# all_numbers = odd_numbers + even_numbers
# print(all_numbers)

# print([1,2,3] * 3)

## EXERCISE
# x = object()
# y = object()

# # TODO: change this code
# x_list = [x] * 10
# y_list = [y] * 10
# big_list = x_list + y_list

# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))

# # testing code
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")

######################### STRING FORMATTING ##################################
# This prints out "Hello, John!"
# name = "John"
# print("Hello, %s!" % name)


# # This prints out "John is 23 years old."
# name = "John"
# age = 25
# print("%s is %d years old." % (name, age))

# # This prints out: A list: [1, 2, 3]
# mylist = [1,2,3]
# print("A list: %s" % mylist)

# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# Exercise
# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s. Your current balance is $%s."

# print(format_string % data)

# String Operations
# astring = "Hello World"
# bstring = 'Hello WOrld'

# astring = " This is sample ' ' "
# print(astring)
# print(len(astring))


# astring = "Hello World"
# print(astring.index("o"))

# astring = "Hello world!"
# print(astring.count("l"))

# astring = "Hello world!"
# print(astring[3:7])

# astring = "Hello world!"
# print(astring[3:7:2])

# astring = "Hello world!"
# print(astring[3:7])
# print(astring[3:7:1])


# astring = "Hello world!"
# print(astring[::-1])


# astring = "Hello world!"
# print(astring.upper())
# print(astring.lower())

# astring = "Hello world!"
# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))

# astring = "Hello world!"
# afewwords = astring.split(" ")

# ############### Exercise ########################################

# s = "Strings are awesome!"
# # Length should be 20
# print("Length of s = %d" % len(s))

# # First occurrence of "a" should be at index 8
# print("The first occurrence of the letter a = %d" % s.index("a"))

# # Number of a's should be 2
# print("a occurs %d times" % s.count("a"))

# # Slicing the string into bits
# print("The first five characters are '%s'" % s[:5]) # Start to 5
# print("The next five characters are '%s'" % s[5:10]) # 5 to 10
# print("The thirteenth character is '%s'" % s[12]) # Just number 12
# print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)

print("hello python")


