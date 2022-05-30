# Problem 2
# Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
# For example:
# stringBits('Hello') → 'Hlo' stringBits('Hi') → 'H' stringBits('Heeololeo') → 'Hello'


# Method 1
def stringBits(word):
    result = ""
    for i in range(len(word)):
        if (i%2) == 0:
            result += word[i]
    print(result)
            
            
stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')
print("\n")


#Method 2
print('Hello'[::2])
print('Hi'[::2])
print('Heeololeo'[::2])


    
