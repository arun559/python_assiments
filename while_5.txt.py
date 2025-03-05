m=int(input("enter ehat table you need :"))
n=int(input("enter the limt of the table :"))
i=1
add=[]
while n>=i:
    add.append(f"{m} * {i} = {m * i}")
    print(add[-1])
    i+=1