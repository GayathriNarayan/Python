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

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd*',
                 'sd+',
                 'sd?',
                 'sd{3}',
                 'sd{2,3}',
                 ]
multi_re_find(test_patterns,test_phrase)