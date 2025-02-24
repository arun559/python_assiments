#food
dosi=10 
idly=5
poori=15
pongal=20
chapathi=15
print("This is menu\n dosi \n poori\n pongal \n idly \n chapathi ")
print("give me the price list ")
print("dosi=10 \n idly=5 \n  poori=15 \n pongal=20\n  chapathi=15")

q =int(input("how may dosi you need :"))
total= dosi *q
gst=(total*18)/100
print("total price ",total)
print(f"gst",gst)
print(f"your total amount :", gst+total)

