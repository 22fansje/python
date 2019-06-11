#File modb_distance.py
#A program to do convert distance
#Made 6/11/19
#By: Jered Fanska

def main():
    kilometers = float(input("Enter a distance in kilometers: "))
    conv_fac = 1.609 #conversion factor 
    #calculating the miles 
    miles = round(kilometers / conv_fac,5)
    print("The distance in miles is: ", miles)
main()