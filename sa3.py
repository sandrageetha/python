string=int(input("Enter the number:"))
string1=list(map(int,input("enter the list:").split()))
if string in string1:
    print("Item found ",string1.count(string),"times in list")

