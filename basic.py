# a =5
#     '''
#     this is basic python 
#     '''

a = {'1':'pending', '2':'approved', '3': 'abcde'}

# filter dict a: so that we can get only values which consists of letters 'a' or 'b' or 'c'

# using dict comprehension 

# res =  {'2':'approved', '3': 'abcde'}

x = {k:v for k, v in a.items() if ('a' or 'b' or 'c') in v}

print(x)

import test

test.run()
