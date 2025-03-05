n=int(input("Give n number "))
i=1
add=[]
while n >= i:
    print(n," this you given number")
    add.append(i)
    i+=1
print(add)
u=sum(add)
print(u)