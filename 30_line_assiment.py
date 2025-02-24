
menu={"juice":{"applie juice":20,"lemon juice":30,"papaya juice":10},
      "Meals":{"pongal":30,"dosai":15,"lemon rice:":25,"idley":8},
      "fast food":{"chikenrice":70,"noodeles":50,"egg rice":55}}
print("(❁´◡`❁)Welcome_Mr_Alone_Shop(❁´◡`❁)\n")
park=input("hello sir are you come in car or bike : ")
if park=="car":
    print("\nSir per hour 100 rs car")
elif park=="bike":
    print("\nsir per hour 10rs bike")
else:
    print("\nthere is no charge sir")
print("\n This is our choice your foode type :\n Juice\n Meals\n Fast food")
floor=input("my food type is ").lower()
if floor== "juice":
    print("can you go to Ground floor ")
    y=input("Sir, this is the Ground Floor. To continue, type 'YES': ").upper()
    if y == "YES":
        print(f"Sir this menu list {menu['juice'] }")
elif floor== "meals":
    print("Go to second floor")
    y=input("Sir, this is the second Floor. To continue, type 'YES': ").upper()
    if y=="YES":
        print(f"sir this your measls {menu['Meals']} ")
elif floor== "fast food":
    print("Go to  first floor")
    y=input("Sir, this is the first Floor. To continue, type 'YES': ").upper()
    if y =="YES":
        print(f"sir this is our menu list {menu['fast food']}")
else:
    print(f"that {floor} not in my hotel sir....")