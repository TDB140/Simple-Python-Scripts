#Program Name: Triangle Area Version 3
#By :Tim Bergen
#date: July 10, 2020
#Description: Prompt user for base length and height of a trinagle in cm's
#             Varify that the values are positive and greater than zero, quit if they are not
#             Calculate area = 0.5 * base * height and convert the value from cm^2 to m^2
#             Output the area, to two decimal places, in an informative way
#

#introduction
print ('Welcome the the area of a triangle calculator.')
print ('All Measurements are taken in centimeters (cm) with the result given in meters squared (m^2)')

#get data from user and check that it is valid
base = float(input('What is the length of the base of the trinagle (cm)? '))
while base <= 0 :
    print("ERROR!  You entered a value that was unusable.  Numbers enetered must be greater than zero.  You entered :", base)
    base = float(input('What is the length of the base of the trinagle (cm)? '))
    
height = float(input('What is the height of the triangle (cm)? '))
while height <= 0 :
    print("ERROR!  You entered a value that was unusable.  Numbers enetered must be greater than zero.  You entered :", height)
    height = float(input('What is the height of the triangle (cm)? '))
    
#calculate area, convert to meters squared with 2 decimal places and output result
area_of_triangle = ((0.5 * base * height)/10000)
print ("The area of the trinagle with a base of ", base, "cm and a height of ", height, "cm is: ", round (area_of_triangle,2), "m^2")
