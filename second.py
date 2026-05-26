company = "Google"
salary = int(input("Enter your salary: "))
HRA = 0.2*salary

print("HRA is: ", HRA)

DA = 0.5*salary
print("DA is: ", DA)
PF = 0.12*salary
print("PF is: ", PF)
gross_salary = salary + HRA + DA
print("Gross Salary is: ", gross_salary)
Tax = 0.1*gross_salary
print("Tax is: ", Tax)
net_salary = gross_salary - Tax
print("Net Salary is: ", net_salary)
total_deduction = Tax + PF
print("Total Deduction is: ", total_deduction)  