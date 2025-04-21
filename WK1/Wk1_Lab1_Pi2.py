# Function six
# declare string variables to pass to function one
str1 = "Hello"
str2 = "World"

# first function named six- takes two string variables 
# prints a label noting it as the first executed function 
# passes the strings to two seprate print methods using comma separation, and concatenate
def six(str,strg):
    print("Function six>")
    print str, strg
    print str + strg

six(str1,str2)
