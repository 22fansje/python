# File: convert.py
# A program to convert Celsius temps to Fahrenheit
# Modified 06/11/19
# By: Jered Fanska

def ctf():
    for i in range(5):
        C = eval(input("What is the Celsius temperature? "))
        F = 9 / 5 * C + 32
        print("The temperature is", F, "degrees Fahrenheit.")
        print(" ")
    


def ftc():
    for i in range(5):
        F = eval(input("What is the fahrenheit temperature?"))
        C = (F-32)*5/9 
        print("The temperature is",Celsius,"degrees celsius.")
        print(" ")

def main():
    print("Convert Celsius to Fahrenheit")
    print("Celsius temperature \t Fahrenheit Equivalent")
    for CCT in range(0,101,10):
        FTE = ( 9 / 5 ) *CCT + 32
        print( CCT,"°C","\t\t\t",CTE,"°F")
    uc = input("Do you want to convert C-->F(c) or F-->C(f) or quit(q):")
    while uc !='q':
        if uc == 'c':
            ctf()
            uc = input("Do you want to convert C-->(c) ro F-->(f) or quit(q): ")
        elif uc == 'f':
            ftc()
            uc = input("Do you want to convert C--F(c) or F-->(f) or quit(q): ")
        elif uc !='c' and uc !='f':
            print("Please put a VALID INPUT!")
            uc = input("Do you want to convert C-->F(c) or F-->C(f) or quit(q): ")
    print("Now exiting...")

main()