#  Problem Set 1a
#  Get user input for annual salary, a fraction to save monthly and total cost of dream house.
#  Assuming an annual return on investment of r = 0.04, use savings*r/12 to accumulate savings,
#  and 0.25 * total cost to calculate down payment,
#  print the number of months required to save the downpayment.
#

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter your monthly savings as decimal: "))
total_cost = float(input("Enter the cost of your dreamhouse: "))
print("Based on a savings of", portion_saved, "of a salary of", annual_salary, "and a house costing", total_cost)

month = 0
current_savings = 0.0
r = 0.04
portion_down_payment = 0.25

#  Monthly income is savings from paycheck + interest from investments
down_payment = portion_down_payment * total_cost
monthly_savings = annual_salary*portion_saved/12

print("Based on", total_cost, "you'll need a down payment of", down_payment)

while current_savings < down_payment :
    month += 1
    interest = current_savings*r/12
    current_savings += (monthly_savings + interest)

print("Months:", month)
#print("Saving", monthly_savings, " per month, you will be able to buy your house in", month, "months.")

#  This code produces the correct answer to two test cases
#  120000, 0.1, 1000000 -> 183
#  80000, 0.15, 500000 -> 105
#  A hidden lesson in the additive value of thrift.
