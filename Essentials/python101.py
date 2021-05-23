#!/bin/python3

#Print string
print("string and things")
print("Hello EveryOne")
print("""Hello Everybody
veryOne multiline""")
print("ya this is " + "a string")

print("\n") #new line

#Math Section

print("Math time")
print(50+50) #add
print(50-40) #sub
print(50*50) #multiply
print(50/50) #divide
print(50*50 - (25/ 5)) 
print(5 ** 6) #power
print(50 % 6) #modulo
print(50 // 6) #number without leftover

#variables and methods

print("\n") #new line

print("Fun with variables and methods")

quote = " all is fair in love and brostep"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

name = "Heath Ledger"
age = 29 #int int(29)
gpa = 3.7 #float(3.7)

print(int(age))
print(int(29.9)) #does not round

print("my name is " + name + " and i am " + str(age) + " years old ")

print("\n") #new line

age += 1
print(age)

birthday = 1

age += birthday
print(age)

print("\n") #new line

#Functions

print("NOW , create some functions")

def who_am_i():
	name1 = "Heath"
	age = 24
	print("my name is " + name + " and i am " + str(age) + " years old ")
	print("this is inside the function")
	
who_am_i()	

#print(name1) name1 not defined
print("\n") #new line
#adding in parameters

def add_one_hundred(num):
		print(num + 100)

add_one_hundred(100)

print("\n") #new line
#add multiple parameters
def add(x,y):
		print(x + y)

add(25,65)		
print("\n") #new line
#using return

def multiply(x,y):
		return x * y

print(multiply(8,9))

def square_root(x):
	return x ** .5

print(square_root(64))

print("\n") #new line
#Boolean Expressions (True or False)
print("Boolean Expressions")
bool1 = True
bool2 = (3*3) == 9
bool3 = False
bool4 = 3*3 == 20
print(bool1,bool2,bool3,bool4)

print(type(bool1))

bool5 = "True"
print(type(bool5))
print("\n") #new line
#Relational and Boolean Operators
greaterThan = 7 > 5
lessThan = 5 < 7
greaterThanEqualTo = 7 >= 7
lessThanEqualTo = 7 <= 7
print(greaterThan,greaterThanEqualTo,lessThan,lessThanEqualTo)

testAnd = (7 > 5) and ( 5 < 7)
testOr = ( 7 > 5 ) or ( 5 < 7 )
testNot = not True

print(testAnd, testOr , testNot)
print("\n") #new line 

#Conditional Statements
print("Conditional Statements")

def soda(money):
	if money >= 2:
		return "You got soda"
	else:
		return "No Soda for U"

print(soda(3))
print(soda(1))			

def alcohol(age , money):
	if (age >= 21) and (money >= 5):
		return "take your alcohol"
	elif (age >= 21) and ( money < 5):
		return "come back with money"
	elif (age < 21) and ( money >= 5):
		return "nice try kiddo"
	else:
		return "poor and young huh !"

			
print(alcohol(14,1))
print(alcohol(34,1))
print(alcohol(25,54))

print("\n") #new line 

#Lists 
print("Lists have brackets")
movies = ["harry mets sally", "lotr", "exorcist" , "malcolmX"]

print(movies[0])
print(movies[0:2])
# print(movies)
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("Jaws")

print(movies)
movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["harry mets sally", "lotr", "exorcist" , "malcolmX"]
person = ["Heath" , "Jake" , "Leah" , "Jeff"]
combined = zip(movies,person)
print(list(combined))

print("\n") #new line 

#Tuples #tuples are static or sth 
print("Tuples have paranthesis and cannot change")
grades = ("A" , "B" , "C" , "D" , "F")
print(grades[1])

#Looping
print("For loops - start to finish of iterate:")

vegatables = ["cucumber", "spinach", "cabbage"]
for x in vegatables:
	print(x)
print("While LOOPS _ execute as long as TRUE")
i = 1
while i <= 10:
	print(i)
	i += 1








