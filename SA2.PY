def rev(s):
    if(len(s))==1:
        return s[0:1]
    else:
        return s[len(s)-1]+rev(s[0:len(s)-1])
    
    
    
string=input("entrt the word:")
print("Word in reverse order is :{}".format(rev(string)))
