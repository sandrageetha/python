try:
    n=int(input("enter the number:"))
    if(n<90 or n>120):
        raise ValueError("abnormal condition")
except Exception as ve:
        print(ve)
