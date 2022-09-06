from functools import reduce 
def sortString(str):
    return reduce(lambda a, b : a + b, sorted(str))
str =input('enter the word')
print(sortString(str))
