
def primetest(x):
    if x==1:
        return False
    else:
        c=0
        for i in range(1,x):
            if x%i==0:
                c+=1
        if c==1:
            return True
        else:
            return False 

with open('myFirstFile.txt', 'w') as f:
    d=int(input("Enter the value for 'd' : "))
    start = 10**(d-1)
    end = 10**d
    for i in range(start,end):
        if primetest(i) and primetest(i+2):
            f.write(str(i)+' '+str(i+2)+'\n')


