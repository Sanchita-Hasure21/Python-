total_days=int(input("enter days :"))
year=total_days//365
month=(total_days-(year*365))//30
remaining_days =total_days-((year*365)-(month*30))
print("year:",year)
print("month:",month)
print("Remaining_days :",remaining_days)