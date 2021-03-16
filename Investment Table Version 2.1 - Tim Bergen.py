#Program Name: Investment Table Version 2
#By : Tim Bergen
#date: July 10, 2020
#Description: Write a program that generates compound interest table for an
#             initial principal amount and a fixed interest rate.
#program must: 1)prompt user to enter -initial investment, annual rate until the interest rate = 0
#              2)the program will output the value of the investment
#                at the end of the last year with a interest rate >0

#gather input on initial investment, annual rate, # of years the principal to be invested
investment_amount = float(input("What is your principal amount invested? $"))
initial_investment = investment_amount
years_invested = 0 #to track the years
annual_interest_rate = 1
                               
while (annual_interest_rate != 0) :
    years_invested = years_invested + 1
    annual_interest_rate = float(input("What is the annual interest rate for year"+ str(years_invested) +" (in percentage)? "))
    investment_amount = (investment_amount * (1 + (annual_interest_rate / 100)))
    
years_invested = years_invested - 1
print("At the end of ", years_invested, "years, your investment will be worth: ${:.2f}".format(investment_amount))
avg_yearly_income = (investment_amount - initial_investment) / years_invested
print("Your average yearly income is: ${:.2f}".format(avg_yearly_income))
    

