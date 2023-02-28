list=list(input("enter the string").split())
count=0
for i in list:
    if i[0].lower()==i[-1].lower():
        count+=1
print("Number of strings:{}".format(count))

