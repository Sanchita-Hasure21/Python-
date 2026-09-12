print ("select TV Category :")
print ("1- B")
print ("2- C")
choice= input(  )
if(choice== "B"):
    cost_price=int(input("Enter cost price "))
    discount=(cost_price*10)/100
    selling_price=cost_price - discount
    print("The Selling price of B is ",selling_price)
elif(choice== "C"):
    inches=int(input("Enter Inches :"))
    if(inches==32):
        cost_price=float(input("Enter cost price "))
        discount=(cost_price*15)/100
        selling_price=cost_price - discount
        print("The Selling price of 32 inches Tv is : ", selling_price )
    elif(inches==55):
        cost_price=float(input("Enter cost price "))
        discount=(cost_price*20)/100
        selling_price=cost_price - discount
        print("The Selling price of 32 inches Tv is : ", selling_price )


