a=[]
b=int(input("Enter the nuber of elements:"))
try:
    for i in range(b):
        d=int(input("Entert the number:"))
        if(d<0):
            print("Enter the positive number:")
        else:
                a.append(d)
    p=0
    c=0
    for i in a:
        for j in range(2,i):
            if(i%j==0):
                c=c+1
                beak
        else:
            p=p+1
    print("composite:",c)
    print("prime:",p)
except valueError:
    print("Enter the input as positive integer value")
