print("select your choice")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divsion")
print("5.Area of circle")
choice=int(input( ))
if(choice==1):
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    sum=num1+num2
    print("The sum is :",sum)
elif(choice==2):
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    sub=num1-num2
    print("The sub is ",sub)
elif(choice==3):
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    mult=num1*num2
    print("The Multiplication is :",mult)
elif(choice==4):
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    Div=num1/num2
    print("The Division is :",Div)
elif(choice==5):
   radius=int(input("enter a radius"))
   area=3.14*radius*radius
   print("Area of circle is :",area)
else:
    print("invalid")


    

    


