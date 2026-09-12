marks1=int(input("Enter marks of sub 1 :"))
marks2=int(input("Enter marks of sub 2 :"))
marks3=int(input("Enter marks of sub 3 :"))
marks4=int(input("Enter marks of sub 4 :"))
marks5=int(input("Enter marks of sub 5 :"))

sum=marks1+marks2+marks3+marks4+marks5

avg=sum/5

percentage=(sum/500)*100
print(sum)
print(avg)
print(percentage)
if(percentage)>90:
    print("OutStanding")
else:
    print("Very Good")

