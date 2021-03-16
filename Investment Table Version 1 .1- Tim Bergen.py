#Program Name: Investment Table Version 1

#By :Tim Bergen
#date: July 10, 2020
#Description: Write a program that generates compound interest table for an
#             initial principal amount and a fixed interest rate.
#program must: 1)prompt user to enter -initial investment, annual rate, # of years
#                                       the principal will be invested
#              2)the program will format a table showing the value of the investment
#                at the end of each year

#gather input on initial investment, annual rate, # of years the principal to be invested
investment_amount = float(input("What is your principal amount invested? $"))
annual_rate_percentage = float(input("What is the annual interest rate (in percentage)? "))
annual_rate = annual_rate_percentage * 0.01 #convert to a decimal
length_of_investment = float(input("How many years will this be invested for?:"))
years_invested = 0 #to track the years

print("Year", "    Balance")
#Calculations
while years_invested < length_of_investment :
    years_invested = years_invested + 1
    investment_amount = (investment_amount * annual_rate) + investment_amount
    print("", years_invested, "      ${:.2f}".format(investment_amount))
    
    
