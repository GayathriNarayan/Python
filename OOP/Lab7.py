# You are provided with the following phrase:
# phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'
# Use python library and try to find:


import re

phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'

# 1. Sequence of digits

#search using regex -- regular expression operations
x1 = re.findall('[0-9]+', phrase)              # re.findall("[\d]+",phrase)
print("Sequence of digits are " +str(x1))
print('\n')


# 2. Sequence of non-digits
x2 = re.findall('[a-zA-Z]+', phrase)            # re.findall("[\D]+",phrase)
print("Sequence of non-digits are " +str(x2))
print('\n')

# 3. Sequence of whitespace
x3 = re.findall('[\s]+', phrase)
print("Sequence of whitespaces are " +str(x3))
print('\n')

#To count number of white spaces in the given phrase
spaces=0
for i in range(0,len(phrase)):
  if(phrase[i]==' '):
    spaces=spaces+1
print("The number of spaces are: ",spaces)
print('\n')


# 4. Sequence of non-whitespace
x4 = re.findall('[\S]+', phrase)
print("Sequence of non-whitespaces are " +str(x4))
print('\n')
# match = re.search(pat, str)


# 5. alphanumeric characters
x5 = re.findall('[\w]+',phrase)
print("Alphanumeric characters are " +str(x5))
print('\n')

# 6. non alphanumeric
x5 = re.findall('[\W]+',phrase)
print("Non Alphanumeric characters are " +str(x5))
print('\n')