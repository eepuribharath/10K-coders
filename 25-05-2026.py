print("Select the menu")
print("1.Veg \n" "2.Non veg")
opt=input("Select your opt :")

if(opt == "1"):
    print("Hello Customer...! you have selected Veg menu")
    print("Veg items are:\n""1.Panner Butter Masala ---------> 350RS\n""2.Panner Briyani ---------> 200Rs")
    items=input("Select your item :")
    if(items =="1"):
        print("Thank You customer...! You ordered Panner Butter Masala")
    elif(items == "2"):
        print("Thank You customer...! You ordered Panner Briyani")



elif(opt == "2"):
    print("Hello Customer...! you have selected Non Veg menu")
    print("Non Veg items are:\n""1.Chicken Briyani--------->250RS\n""2.Mutton Briyani--------->700Rs")
    items=input("Select your item :")
    if(items =="1"):
        print("Thank You customer...! You ordered Chicken Briyani")
    elif(items == "2"):
        print("Thank You customer...! You ordered Mutton Briyani")

    

else:
    print("Please select a valid option")