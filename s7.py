try:
    print("resource open")
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    a=(num1/num2)
except ZeroDivisionError as e:
    print("division using zero:",e)
except ValueError as e:
    print("inavlid :",e)
else:
    print(a)
finally:
    print("resource closed")
