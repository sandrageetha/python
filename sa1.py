def word(w,n):
    
    l=[]
    for i in range(0,n):
        l.append(w)
    return l
w=input("enter the word:")
n=int(input("Enter the number:"))
m=word(w,n)
for i in range(0,n):
    print(m[i])
