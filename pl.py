
def palindrome():
    n = input()
    l = n[::-1]
    k = 0
    if n ==l:
        found = True
    else:
         found = False

    if found:
        for i in range(0,len(n)):
            k = k+int(n[i])
    return k
    
print(palindrome())
