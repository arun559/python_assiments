i=int(input("enter the first  number : "))
j=int(input("enter the last number : "))
su=[]
for i in range (i,j): #1    10
    su.append(i)
    print("loop",i)
print("Grand total ",sum(su))