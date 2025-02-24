print("Alone engineering college ")
entery=input("what your proof id / Worker / parents : ").lower()

#gate 2
if entery=="worker":
    print(f"Go to gate no 2")
    print("come here Fill the datas")
    name=input("enter your name : ")
    place=input("where are you from : ")
    why=input("what the reson : ")
    intime=int(input("enter your enter hour : "))
    mi=int(input("what is min : "))
    print(f"your name is {name} you from {place} your comming reson was {why} and you come time is {intime}:{mi}")
elif  entery=="parents":
    print("Go to Hostel office : ")
    sname=input("what is the son name : ")
    year=int(input("Which year your students : "))
    dep=input("what is the department : ").upper()

    if year==1:
        if dep=="ECE" :
            print("Go  first floor and room no is 1")
        elif dep=="MEC" :
            print("Go  first floor and room no is 2")
        elif dep=="EEE" :
            print("Go  first floor and room no is 3")
        elif dep=="EEE" :
            print("Go  first floor and room no is 4")
        else:
            print("give corret deprment")
    elif year==2:
        if dep=="ECE" :
            print("Go  second floor and room no is 1")
        elif dep=="MEC" :
            print("Go  second floor and room no is 2")
        elif dep=="EEE" :
            print("Go  second floor and room no is 3")
        elif dep=="EEE" :
            print("Go  second floor and room no is 4")
        else:
                print("give corret deprment")
    elif year==3:
        if dep=="ECE" :
            print("Go third floor and room no is 1")
        elif dep=="MEC" :
            print("Go third floor and room no is 2")
        elif dep=="EEE" :
            print("Go third floor and room no is 3")
        elif dep=="EEE" :
            print("Go third floor and room no is 4")
        else:
            print("give corret deprment")
    elif year==4:
        if dep=="ECE" :
                print("Go fouth floor and room no is 1")
        elif dep=="MEC" :
            print("Go fourth floor and room no is 2")
        elif dep=="EEE" :
            print("Go fourth floor and room no is 3")
        elif dep=="EEE" :
            print("Go fourth floor and room no is 4")
        else:
            print("give corret deprment")
    else:
        print("there is no one")       
elif entery=="id":
    print(f"Go to gate 1")
    user_id=input("your user name : ").lower()
    password=int(input("type your password : "))
    A={"arun":1,"swetha":2,"krishna":3,"kee":4}                 #user name 
    if user_id in A and A[user_id] == password:
          print(f"welcome  {user_id}")
    else:
         print("enter valide user_id &pasword")
else:
    print("Give correct respoins")
#gate 1




    
"""
if id=="ECE":
    print(f"Go to gate on 1 ")
    cls:["first_year","second year"]
elif id=="CS":
    print("Go to gate on 2")

elif id=="worker":
    print("Go to gate no 3")

elif id=="parents":
    print("Can wait on main office or Hostel office")
"""



'''print("👀......welcome come to Alone Bar.....👀")
menu={"hot":["whyiskey","vodka","rum","brandy"],
      "cold":["Kingfisher Strong","Royal_Challenge","thunderbolt","tuborg"]}

my_order=input("enter your type : ")

if my_order in menu:
 print(f"Your menu in the brand list{menu[my_order]} ")
else:
 print("That {menu[my_order]} no in the bar")
 '''
 #juice=Ground_floor

