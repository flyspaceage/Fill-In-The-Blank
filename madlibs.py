# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# Add your own code and notes here

speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000. #2.7ghz

print speed_of_light / cycles_per_second

cycle_distance = speed_of_light / cycles_per_second
print cycle_distance

#variables can vary
#variables may be used in their own assignment statements
# equal sign means assignment (think arrow sign)

age = 7
days_in_year = 365.25

print age * days_in_year

# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Add your own code and notes here

word = "assume"

print word[3]
print word [3:4]
print word [4:6]
print word [:2]
print word [2:]

# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1  

# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

# Add your own code and notes here

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20: 
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"
    

if <TestExpression>:
	<block>:

def bigger(x):
	if x<0:
	x=-x
return x

def bigger (x,y):
	if x>y:
		return x
	return y

def bigger (a,b):
	if a>b:
		return a
	else:
		return b
def is_friend(name):
	if name[0]=="D":
		return True
	else:
		return False

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
    if name[0]=="D":
        return True
    if name[0]=="N":
        return True
    else:
        return False

def is_friend(name):
	return name[0]=="D" or name[0]=="N"


print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False


# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

# Add your own code and notes here

# This code demonstrates a while loop with a "counting variable"
i = 0
while i < 10:
    print i
    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

def print_numbers(n):
	i = 1
	while i <= n:
		print ii = i + 1

print print_numbers

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here


def weekend(day):
    return day == 'Saturday' or day == 'Sunday'

def weekend(day):
    return day in ('Saturday', 'Sunday')
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).


def countdown(x):
    while x > 0:
        print x
        x = x - 1
    print "Blastoff!"


print countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))
    
def median(a, b, c):
    largest = biggest(a, b, c)

    if a == largest:
        between = bigger(b, c)
        return between
    if b == largest:
        between = bigger(a, c)
        return between
    if c == largest:
        between = bigger(a, b)
        return between 

#random noun
from random import randint

def random_noun ():
	random_num = randint(0,1)
	if random_num == 0:
		return "sofa"
	else:
		return "llama"

# random verb
from random import randint

def random_verb():
    random_num = randint(0,1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

# mad libs take 1
def word_transformer(word):
	if word == "NOUN":
		return random_noun()
	if word == "VERB":
		return random_verb()
	else:
		return word[0]


# madlibs stage 2 work session 4
def process_madlib(madlib):
    processed = ""
    index = 0
    box_length = 4
    while index < len(madlib):
        frame = madlib[index:index + box_length]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add)==1:
            index+=1
        else:
            index+=4
    return processed

# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

# Add your own code and notes here

# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    if index=0:
        return [1]


#print how_many_days(1)
#>>> 31

#print how_many_days(9)
#>>> 30

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month):
    return days_in_month[month - 1]

print how_many_days(1)

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print countries[1][1]


# Given the variable countries defined as:
#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

print countries[0][2] / countries[2][2]



# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

#['Moe','Larry','Shemp']

# but does not create a new List
# object.

print stooges
stooges[2] = 'Shemp'
print stooges

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

def replace_spy(x):
    x[2] = x[2] + 1


# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print spy
#>>> [0,0,8]

#list operations

#append
<list>.append(<element>)
stooges = ["Moe", "Larry", "Curly"]
stooges.append("Shemp")
#adds "Shemp" as 4th item in list

#plus
<list> + <list>

#len
len(<list>)
    len([0,1]) --> 2
    len(["a", ["b", ["c"]]]) --> 2
    len("Smash") -->5

#Summarize following concepts:
# Structured data
# Mutability
# The difference between append and +

# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4152219158/m-48204891

def print_all_elements(p):
    for e in p:
        print e

myList = [1, 2, [3, 4]]
print_all_elements(myList)

# Add your own code and notes here

def print_all_elements(p):
    i = 0
    while i < len(p)
        print p[i]
        i = i + 1

# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing
    

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country


# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result



print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134


# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(U):
    count = 0
    for x in U:
        if x[0] == 'U':
            count = count + 1
    return count

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.


def find_element(x,y):
    if y in x:
        return x.index(y)
    else:
        return -1
    

print find_element([1,2,3],3)
#>>> 2

#2.7 HOW TO SOLVE PROBLEMS
# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    return days

    # Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325398

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.

def isLeapYear(year):
    return True

def daysInMonth(year, month):
    return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
    return days

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()
#define nextDay assuming all months have 30 days
def nextDay (year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    return

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1< year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def isLeapYear(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 of month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return
    return 30 

    


