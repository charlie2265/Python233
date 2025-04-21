# Charlie Ritter

import locale
locale.setlocale(locale.LC_ALL, '')


# Function one
# declare string variables to pass to function one
str1 = "Hello"
str2 = "World"

# first function named one- takes two string variables 
# prints a label noting it as the first executed function 
# passes the strings to two seprate print methods using comma separation, and concatenate
def one(str,strg):
    print("Function one>")
    print(str, strg)
    print(str + strg)

one(str1,str2)


# Function Two
# declare string variables to pass to function two
name = "Charlie"
school = "MHCC"

# execute two print statements 
# one with format method and the other demonstrating 
# the use of tabs and next-line with escape characters
def two(str1, str2):
    print("\nFunction two >")
    print("My name is {} and I go to {}.".format(str1, str2))
    print("My\t name\t is\t {} \nand\t I\t go\t to\t {}.".format(str1, str2))

two(name,school)


# Function three 
# Replicate the output of function two using f-string technique
# pass the same string variables. 
def three(str1, str2):
    print("\nFunction three >")
    print(f"My name is {str1} and I got to {str2}.")
    print(f"My\t name\t is\t {str1} \nand\t I\t got\t to\t {str2}.")

three(name, school)


# Function four
# decalre string, integer, and float variable
fruit = "apples"
qty = 5
price = 4.5 

# Funtion four - pass the three variables to 
# print "I bought 5 pounds of apples for $4.50" no local
def four(str1, int1, float1):
    print("\nFunction four >")
    print("I bought {} pounds of {} for ${:.2f}".format(str1, int1, float1))

four(qty,fruit, price)


# Function five - Replicate the output of function four using locale to format currency
def five(str1, int1, float1):
    fmt_price = locale.currency(float1)
    locale.setlocale(locale.LC_ALL, 'fr_FR')
    fmt_price = locale.currency(float1)

    print("\nFunction five >")
    print("I bought {} pounds of {} for {}\n".format(str1, int1, fmt_price))

five(qty, fruit, price)

# # Python2 - Run seperatley - 
# # Function 6 
# # declare string variables to pass to function one
# str1 = "Hello"
# str2 = "World"

# # first function named one- takes two string variables 
# # prints a label noting it as the first executed function 
# # passes the strings to two seprate print methods using comma separation, and concatenate
# def one(str,strg):
#     print("Function one>")
#     print str, strg
#     print str + strg

# one(str1,str2)

    
