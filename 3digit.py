def add():
    num=int(input("enter any three digit number :"))
    sums=0
    rem=num%10
    sums=sums+rem
    num=num//10

    rem=num%10
    sums=sums+rem
    num=num//10

    rem=num%10
    sums=sums+rem
    num=num//10

    print("the sum of 3digit is ",sums)

add()

    