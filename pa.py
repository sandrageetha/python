def sum_of_digit(n):
    if n==0:
        return(0)
    elif n==1:
        return 1
    else:
        return n+sum_of_digit(n-1)

num=int(input("enter the number:"))
print("sum of digits:%d"%sum_of_digit(num))



