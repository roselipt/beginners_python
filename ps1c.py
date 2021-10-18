#  Problem Set 1c, MIT Open Course 6.0001 from 2016

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
        #print(after_raise.format(month, annual_salary))

print("Months:", month, "at savings rate of", portion_saved)
#print("Saving", monthly_savings, " per month, you will be able to buy your house in", month, "months.")

#  For the bisection search, the assignment suggests rethinking portion_saved as an integer
p_s_int = 25
lower_bound = 0
upper_bound = 10000
portion_saved = p_s_int/upper_bound
print("Portion saved is", portion_saved)


#  This is the "close enough" amount to stop the search
epsilon = 100
found = False
#  Rest starting balance and salary; 
current_savings = 0
monthly_savings = annual_salary*portion_saved/12

again = True
#
while (not found) and (again) :
    current_savings = 0
    #monthly_savings = annual_salary*portion_saved/12
    #  Calculate savings after 3 years at given rate
    for i in range(36) :
        interest = current_savings*r/12
        current_savings += interest
        current_savings += monthly_savings
        #  Every 6 months recalculate salary
        if (i % 6 == 0) and (i != 0) :
            annual_salary *= (1 + semi_annual_raise)
            monthly_savings = annual_salary*portion_saved/12
    #  After for loop current_savings is after 36 months
    print("Testing for rate {:.6f}".format(portion_saved))
    if abs(down_payment - current_savings) < epsilon :
        found = True
        print("{:.2f} after 3 years at {:.6f}".format(current_savings, portion_saved))
    else :
        #  Bisection search here
        #  Calculate next guess for portion_saved
        if current_savings < down_payment :
            lower_bound = p_s_int
            
        else :
            upper_bound = p_s_int
        p_s_int = int(lower_bound + (upper_bound-lower_bound)/2)
        portion_saved = p_s_int/10000

    print("{:.6f} yields {:.2f}".format(portion_saved, current_savings))
    arg = input(" Would you like to see the next guess?")
    if arg != 'y' :
        again = False
print("The rate that works in 36 months is {:.4f}".format(portion_saved))


