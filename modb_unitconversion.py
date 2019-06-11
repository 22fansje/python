#File name modb_unitconversion.py
#Program to convert messurements
#Made 6/11/19
#By Jered Fanska

def main():
    # grab raw input
    feet, trash = input("How many inchs are in: ").split() # two variables, feet is the number | trash is the extra wording; split breaks the input at the space
    convertion_factor = 12
    inchs = convertion_factor * float(feet)
    print("There is",inchs,"inchs in ",feet,"ft.")
main()