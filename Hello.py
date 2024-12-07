import sys #system functions and parameters
from datetime import datetime as dt #using an alias

#Importing - Importing is important
print(sys.version)

# Strings
print("Hello, World!")
print('Hello, World!')
print("""This string runs
multiple lines""") # triple quotes for multiple lines
print( "This is a "+"string!") #we can concatenate strings
print(' \n') # new line
print("Test that new line out")

print ('\n')
       
#Math
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 / 6) #division with remainder
print(50 % 6) #modulo - takes what is left over
print(50 // 6) #no remainder

print("\n")

# variables and methods
age = 36 #int
name = "Dusty" #string
gpa = 3.7 #float

print(int(age))
print(int(35.1))
print(int(35.9)) #won't round

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowecase
print(quote.title()) #titlecase
print(len(quote)) #count characters

print("My name is "+name+" and I am "+str(age)+" years old. ")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print("\n")
#Functions - Reusable block of code (like a program)

def who_am_i(name,age):
    print(f"My name is {name} and I am {age} years old")

who_am_i("Dusty", 36)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

result1 = multiply(7,7)
result2 = multiply(8,8)
print(result1 + result2)

def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #new line
    print('\n')

nl()
#Boolean Expressions (True or False)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()
#Relational and Boolean Operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
equals = 7 == 7
not_equals = 7 != 8

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7> 5) and (5 > 7) #False
test_or = (7 > 5) or (5 > 7) #True
test_or2 = (7 > 5) or (5 > 7) #True
test_not = not True #False






nl()
# Conditional Statements - if/else

def drink(money):
    if money >= 2:
        return "You'e got yourself a drink!"
    else:
        return "No drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too young and too poor."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()
# For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for veggies in vegetables:
    print(veggies)

for i in range(5):
    print(i)

word = "Python"
for letter in word:
    print(letter)

# While loops - execute as long as True
i = 1

while i < 10:
    print(i)
    i += 1

nl()

# Lists - Have brackets {} - everything inside is called an item

movies = ["Star Wars", "The Hobbit", "Lord of The Rings", "Pulp Fiction"]

print(movies[1]) #return the second item in the list - index
print(movies[0]) # return the first item in the list
print(movies[1:3]) # returns the first number given until right before the last number given
print(movies[1:4]) # returns 1-3
print(movies[1:]) # returns 1-end
print(movies[:1]) # returns everthing before 1
print(movies[:2]) 
print(movies[-1]) # grabs last item

print(len(movies)) # count the items in the list
movies.append("JAWS") # add and item to the end of our list
print(movies)

movies.insert(2, "Hustle")
print(movies)

movies.pop() # removes the last item
print(movies)

movies.pop(0)
print(movies)

amber_movies = ['Just Go With It', "50 First Dates"]
our_favorite_movies = movies + amber_movies #combine lists
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1]= 83
print(grades)

nested_list = [[1, 2, 3], [4, 5,6], [7,8,9]]
print(nested_list[1][2])

#Tuples - Immutable (can't be changed)
coordinates = (40.7128, 74.0060) #New York
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
student = ("John Doe", 8675309, "Computer Science")

print(student[1])

nl()
# Dictionaries - key/value pairs {}

drinks = {"White Russian" : 8, "Old Fashioned": 12, "Lemon Drop": 5} # drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr, Frond"] # add a new key/value pair
print(employees)
employees.update({"Sales": ["Andie", "Ollie"]}) # add a new key/value pair
print(employees)

drinks['White Russian'] = 9
print(drinks)

print(drinks.get("White Russian"))

nl()
#Advanced Strings

my_name = "Dusty"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a senstence."
print(sentence[:4])

print(sentence.split()) #delimiter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "               hello       "
print(too_much_space.strip())

print("A" in "Apple") # return True
print("a" in "Apple") # return False - case sensitve

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

#user_input = input("Enter yes or no: ")
#if user_input.lower().strip() == "yes":
#    print("You agree!")
#else:
#    print("You disagree!")

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")

print(sys.version)
print(dt.now())