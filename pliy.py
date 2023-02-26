def factors(y):
    flist = []
    for i in range(1,y+1):
        if y%i ==0:
            flist = flist+[i]
    return flist
def isprime(y):
    if factors(y) == [1,y]:
        return True
def primeupto(y):
    plist = []
    for i in range(1,y+1):
        if isprime(i):
            plist = plist + [i]
    return plist
print(primeupto(5))
def nprime(y):
    (count , i, nplist) = (0,1,[])
    while count < y:
        if isprime(i):
          (count , nplist) = (count +1,nplist+[i])
        i = i+1
    return nplist
print(nprime(5))
