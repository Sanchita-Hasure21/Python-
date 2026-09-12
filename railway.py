print("========================================")
print("        RAILWAY TICKET BOOKING          ")
print("========================================")

name=input("Enter Passenger name : ")
age=int(input("Enter Passenger Age : "))
gender=input("Enter gender (M/F) :")
ticket_type=input("Enter ticket type (Slepper/AC :)")
distance=float(input("Enter Distance (KM): "))

available_seats = 10
tickets = int(input("Enter number of tickets : "))
remaining_seats =available_seats-tickets 


#seatss availability check 
if tickets > available_seats:
    #print("\n Not enough seats available .")
    #print("available seats : ", available_seats )
    
else:
    print("\nSelect class")
    print("1. General")
    print("2. Sleeper")
    print("3. AC 3 Tier")
    print("4. AC 2 Tier")

    choice=int(input("Enter your choice :"))
    #calculate fare per Km

    if choice==1:
        class_name="General"
        rate=1.00
    elif choice==2:
        class_name="Sleeper"
        rate=1.50
    elif choice==3:
        class_name="AC 3 Tier"
        rate=2.50
    elif choice==4:
        class_name="AC 2 Tier"
        rate=3.00
    else:
        print("Invalid class")
        exit()

    #calculate basic fare 
    Basic_fare = distance * rate 

    #calculatte discount 
    if age <5:
        discount_percent=100
        discount= Basic_fare
    elif age>=60:
        discount_percent=20
        discount=Basic_fare*20/100
    elif age>=5 and age<=11:
        discount_percent=50
        discount=Basic_fare*50/100
    else:
        discount_percent=0
        discount=0

    #fare after discount 
    fare_after_discount= Basic_fare - discount  

    #booking charge 
    booking_charge =50

    #gst calculations
    gst=fare_after_discount*5/100

    #final amount 
    total_amount=fare_after_discount *booking_charge *gst

    #print ticket 

    print("\n========================================")
    print("            RAILWAY TICKET                ")
    print("========================================")

    print("Passenger Name    :",name)
    print("Passenger Age   :",age)
    print("Distance   :",distance,"KM")
    print("Class    :",class_name)
    print("Rate per KM   :Rs.",rate)

    print("----------------------------------------")
    print("Basic Fare  :Rs.",Basic_fare)
    print("Discount  :Rs.",discount)
    print("Discount % :",discount_percent,"%")
    print("Fare After Discount :Rs.",fare_after_discount)
    print("Booking Charge :Rs.",booking_charge)
    print("GST (5%) :Rs.",gst)
    print("numbers of seats Booked :",tickets)
    print("remaining seats :",remaining_seats)
    print("----------------------------------------")










