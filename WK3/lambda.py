# Lambda is the anonymous function that is defined without 
# a name. 
# normal functions are defined using the def keyword
# lambda functions are defined using the lambda keyword
# They are single expression functions that are not necessarily 
# bound to a name. 
# They cant use regular Python statement and always include an 
# implicit return statement.
# Can have any number of arguments but only one expression
# the expression is evaluated and returned.
# lambda functions can be used wherever function objects are required

# create list of numbers from 1 - 20
# unpack using the  *
my_list = [*range(0, -22, -2)]
print("List:", my_list)

# store filter object that performs the lambda function on the iterable
evens_list = filter(lambda x: x % 2 == 0, my_list)

# builds a list of the filtered object and stores in list_output
list_output = list(evens_list)

# prints constructed list
print(list_output)
print(evens_list)







# print("map using functions")

# def multiply2(x):
#     return x * 2

# map_output = map(multiply2, [1,2,3,4])

# list_map_output = list(map_output)
# print(list_map_output)
# print(type(list_map_output))

# print("map using lambda")

# map_output1 = map(lambda x: x*2, [1,2,3,4])
# list_map_output1 = list(map_output1)
# print(list_map_output)







# double = lambda x: x * 2

# print(double(5))
# print(double(6))

# def doub(x):
#     return x * 2
# print(doub(20))