seconds=int(input("Enter Seconds"))
hour=seconds//3600
Minutes=(seconds-(hour*3600))//60
remaining_seconds=seconds-((hour*3600)-(Minutes*60))

print("Hour:",hour)
print("Minutes:",Minutes)
print("Remaining seconds:",remaining_seconds)

