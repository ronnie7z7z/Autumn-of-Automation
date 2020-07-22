
def paltest(x):
    a = str(x)
    b = ""
    for i in range(len(a)):
        b = b + a[len(a)-1-i]
    if a==b:
        return True
    else:
        return False
   
    

a=int(input("Enter a palindrome : "))
while True:
    a += 1
    if paltest(a):
        break
print(a)
