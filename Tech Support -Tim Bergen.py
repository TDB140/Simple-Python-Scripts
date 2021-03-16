#Program Name:Tech Support
#By :Tim Bergen
#date: July 9, 2020
#Description: User will be asked if the ailing computer beeps on Start up and if the hard drive spins
# Use if-else statements

#first if - else is to check to see if the computer beeps
beep_check = input("Does the computer beep when powered on? [Y/N]")
drive_spin = input("Does the drive spin when powered on? [Y/N]")
if beep_check == "Y" :
#the computer beeps, now check to see if the drive spins
    if drive_spin == "Y" :
        print("Contact Tech Support")
    else :
        print("Check drive cables")
#the computer doesn't beep, so check to see if the drive spins
else :   
    if drive_spin == "Y" :
        print ("Check the speaker contacts.")
    else :
        print ("Bring computer to repair centre")
    
