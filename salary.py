basic=int(input("Enter Basic Salary :"))

PF=basic*12/100
TA=basic*3/100
DA=basic*4/100
HRA=basic*7/100

Netsalary=basic+DA+HRA+TA-PF
print("PF :",PF)
print("TA :",TA)
print("DA :",DA)
print("HRA :",HRA)
print("Netsalary:",Netsalary)

