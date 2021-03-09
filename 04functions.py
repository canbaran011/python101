# FUNCTIONS

def myFunction():
    print("this is function")

myFunction()

def funnyWithArgs(username , greeting):
    print("Hello %s , From funny , I wish u %s" %(username,greeting))

funnyWithArgs("can baran","HEOEEOEH")    

def sum_two_numbers(a , b):
    return a + b
sum_two_numbers(2 ,3)

## Exercise


# Modify this function to return a list of strings as defined above
def list_benefits():
    benefits = ["ben1","ben2"]
    return benefits

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()












