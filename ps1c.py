#  Problem Set 1b, MIT Open Course 6.0001 from 2016

#  (1c)  Asks for a bisection search to find the savings rate necessary to achieve a particular
#  goal: a down payment of 0.25 of $1M in 3 years,
#  assuming 150000 salary and 0.07 semi-annual raise.
#  Also count the number of steps. 

#  (1b)  Adds a semiannual raise to be asked for as input as decimal and awarded every six months.

#  (1a)  Get user input for annual salary, a fraction to save monthly and total cost of dream house.
#  Assuming an annual return on investment of r = 0.04, use savings*r/12 to accumulate savings,
#  and 0.25 * total cost to calculate down payment,
#  print the number of months required to save the downpayment.
#

#annual_salary = float(input("Enter your annual salary: "))
#portion_saved = float(input("Enter your monthly savings as decimal: "))
#total_cost = float(input("Enter the cost of your dreamhouse: "))
#semi_annual_raise = float(input("Enter your semi annual raise: "))
#print("Based on a savings of", portion_saved, "of a salary of", annual_salary, "and a house costing", total_cost)

#annual_salary = float(120000)
#portion_saved = float(.05)
#total_cost = float(500000)
#semi_annual_raise = float(.03)

annual_salary = float(150000)
portion_saved = float(.25)
total_cost = float(1000000)
semi_annual_raise = float(.07)

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
    if month % 6 == 0 :
        annual_salary *= (1 + semi_annual_raise)
        monthly_savings *= (1 + semi_annual_raise)
        after_raise = "{} raise to {:.2f}"
        print(after_raise.format(month, annual_salary))

print("Months:", month)
#print("Saving", monthly_savings, " per month, you will be able to buy your house in", month, "months.")

#  This code produces the correct answer to two test cases
#  120000, 0.1, 1000000 -> 183
#  80000, 0.15, 500000 -> 105
#  A hidden lesson in the additive value of thrift.
