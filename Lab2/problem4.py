# Problem 4
# Given a string, return a string where for every char in the original, there are two chars.
# doubleChar('The') → 'TThhee' 
# doubleChar('AAbb') → 'AAAAbbbb' 
# doubleChar('Hi-There') → 'HHii--TThheerree'


def doubleChar(str):
    result = ''
    for char in str:
        result = result + char + char
    print(result)

doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')




