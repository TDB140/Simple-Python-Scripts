#Program Name: mini task- Bilbo's Eggs
#By :Tim Bergen
#date: July 9, 2020
#Description: User will be asked for the number of eggs to be purchased and then calculates the bill
# Use if-else ladder

number_of_eggs_required = int(input("Enter the number of eggs? "))
#elif statements to figure out the cost per egg based of the number of eggs requested
if number_of_eggs_required > 131 :
    dollars_per_dozen = 0.35
    cost_per_egg = (0.35 / 12)
elif number_of_eggs_required > 71 :
    dollars_per_dozen = 0.4
    cost_per_egg = (0.4 / 12)
elif number_of_eggs_required > 47 :
    dollars_per_dozen = 0.45
    cost_per_egg = (0.45 / 12)
else :
    dollars_per_dozen = 0.5
    cost_per_egg = (0.5 / 12)
#output - display the cost per dozen and cost per egg the calculate and display the total cost  
print("Your cost is $", "{:.2f}".format(dollars_per_dozen), "per dozen or $", "{:.2f}".format(cost_per_egg)," per egg.")
total_cost = (cost_per_egg * number_of_eggs_required)
print("Your bill comes to $", "{:.2f}".format(total_cost))
