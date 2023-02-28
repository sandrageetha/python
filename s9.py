class validate(Exception):pass
try:
    username="meera"
    password="meera@12"
    user=input("enter the username:")
    passw=input("enter tha password:")
    if(username!=user or password!=passw):
        raise validate("invalid credential")
    else:
        print("login")
except validate as e:
    print(e)
