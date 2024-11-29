num=int(input("Enter the number"))
fact=1
if num<0:
    print("Factorial does not exist")
if num==0:
    print("Factorial is 1")
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print(fact)
    