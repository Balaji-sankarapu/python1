def reverse(text):
    str=""
    i=len(text)-1
    while(i>=0):
        str=str+text[i]
        i=i-1
    return str
string=input("Enter the text")
print(reverse(string))
