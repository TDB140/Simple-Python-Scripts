#Payroll Calculations

#Date: July 8, 2020
#Assignment Requirements
#Collects input from a user from a console
#processes this input calculating specific formulas
#outputs the result of the calculations in a useful format to the console

#prompt user for inputs
name_first = input('What is your first name? ')
name_last = input('What is your last name? ')
pay_period_hours = float(input('How many hours did you work this pay period? '))
while pay_period_hours <= 0 :#validate
    print("You must enter a vaule that is  greater than 0. Try again. You entered ", pay_period_hours)
    pay_period_hours = float(input('Reenter how many hours you worked this pay period? '))

pay_rate = float(input('What is your hourly rate of pay? $'))
while pay_rate <= 0 :#validate
    print("You must enter a vaule that is  greater than 0. Try again. You entered ", pay_rate)
    pay_rate = float(input('What is your hourly rate of pay? $'))

have_valid_entry = False
while not have_valid_entry :
    tax_exempt_status = input("Are you are tax exempt. (Y/N) : ")
    tax_exempt_status = tax_exempt_status.upper() #convert to capital letter
    if ((tax_exempt_status != "Y") and (tax_exempt_status != "N")) :
        print (" You must enter Y or N.  Try again.  You entered ", tax_exempt_status)
    else  :
        have_valid_entry = True; 
        
if tax_exempt_status == "N" : 
    #if N we need to find tax rate
    tax_rate_percent = float(input('What is your rate of taxation? (%)'))
    #inset a check that this is btwn 1-100%
    while   tax_rate_percent <=1 or tax_rate_percent >= 100 :
                print('You must enter a vaule that is between 1 and 100%. Try again. You entered ', tax_rate_percent) 
                tax_rate_percent = float(input('Please re-enter What is your rate of taxation? (%)'))    
    tax_rate = (tax_rate_percent * (0.01))
else :
    tax_rate = 0

#calculations
gross_pay = (pay_period_hours * pay_rate)   
deductions = (gross_pay * tax_rate)
net_pay = (gross_pay - deductions)

#test outputs
print('------------------------------------------------------')
print('Pay stub for :',name_last + ", " + name_first)
print('Number of hours worked this pay period: ', pay_period_hours)
print('Pay rate:                              $', pay_rate) 
print('                                     ------------')
print('Gross pay:                             $', "{:.2f}".format(gross_pay))
print('Deductions:                           -$', "{:.2f}".format (deductions))               
print('                                     ------------')
print('Net pay:                               $', "{:.2f}".format(net_pay))
print('------------------------------------------------------')

