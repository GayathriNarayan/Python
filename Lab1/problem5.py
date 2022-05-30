# Problem 5:
# You are given two variables: age = 4 name = "Sammy"
# Use print formatting to print the following string: "Hello my dog's name is Sammy and he is 4 years old"


age = 4 
name = "Sammy"

str = "Hello my dog's name is {} and he is {} years old"
print(str.format(name, age))

# print("Hello my dog's name is %s and he is %s years old" % (name, age))

