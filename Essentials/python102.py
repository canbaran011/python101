#!/bin/python3

#Importing
print("Importing is important::")

import sys #system functions and parameters
from datetime import datetime as dt #importing with an alias

print(dt.now())

def newLine():
    print('\n')

newLine()

print("hey you")

#Advanced Strings
print("Advanced Strings:")
myName = "CanBaranG"
print(myName[0]) #first initial
print(myName[-1]) #last letter

sentence = "This is a sentence"
print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word
print(sentence[0]) #first word

print(sentence.split()) #split sentence by delimeter

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))


quoteception = "I said , 'give me all the money'"
print(quoteception)

quoter = "Come and , \"see what happens\""
print(quoter)



print("A" in "Apple")
letter = "A"
letter2 = "a"
word = "Apple"
print(letter in word)
print(letter2 in word)

print(letter.lower() in word.lower())
wordTwo = "Bingo"

print( (letter.lower() in word.lower()) and not (letter.lower() in wordTwo.lower()) )
tooMuchSpace = "        hello          "
print(tooMuchSpace.strip())

fullName = "eath Adams"
print(fullName.replace("eath","Heath")) 
print(fullName.find("Adams")) 

movie = "The Hangover"
print("My fav movie is {}".format(movie) )

def favoriteBook(title, author):
    fav = "My fav book is \"{}\" ,which is written by {}.".format(title,author)
    return fav

print(favoriteBook("WhiteWolf", "John Wein"))

newLine()
#Dictionaries
print("Dictionaries and values")
drinks = {"White Russians" : 7, "Old Fashion" : 10, "lemon Drop" : 12} #drink is key ,price is value
print(drinks)

employees = {"finance" : ["Bob" , "Linda", "Tinda"],"IT" : ["gene" , "lousie" , "matt"], "HR" : ["Jimmy" , "Morty"]}
print(employees)

employees["Legal"] = ["Mr.Front"] #add new key : valu pair
print(employees)

employees.update({"Sales" : ["Andie","Ollie"]})
print(employees)

drinks["White Russians"] = 8
print(drinks)

print(drinks.get("White Russians"))
print(drinks.get("Martini"))
print(drinks["White Russians"])

#List and dictionaries
movies = ["Harry mets Sally" , "The Hangover" , "Perks of Wallflower" , "Dark Lord"]
person = [ "Heath" , "Can" , "Leah" , "Jess"]
combined = zip(movies,person)
movie_dictionary = {key : value for key ,value in combined}

print(movie_dictionary)



