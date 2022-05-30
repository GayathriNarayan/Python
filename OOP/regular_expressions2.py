import re
def multi_re_find(patterns,phrase):
    
    for pattern in patterns:
        print("Searching the phrase using re check: %r" % pattern)
        print(re.findall(pattern,phrase))
        print('\n')
        
        
# A pattern followed by the meta-charcter * is repeated zero or more times.
# Replace the * with + and the pattern must appear at least once.
# Using? pattern appears zero or one time.
#{m}
#{m,n}

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns = [r'\d+', #digits
                 r'\D+', #non-digits
                 r'\s+', #whitespace
                 r'\S+', #non-whitespace
                 r'\w+', #alphanumeric char
                 r'\W',  #non-alphanumeric
                 ]
multi_re_find(test_patterns,test_phrase)