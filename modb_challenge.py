def main():
    #Get's info on the user's name than greets them
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    print("Hello, %s %s!"%(first_name,last_name))
    print()

    #Lists the foods avaliable
    food = ['Cookie', 'Steak', 'Ice cream', 'Apples']
    for food in food:
        print (food)

    #showing age in days, weeks and months
    print()
    age_in_years = float(input("How old are you?: "))
    days_in_years = age_in_years * 365
    weeks_in_years = age_in_years * 52.143
    months_in_years = age_in_years * 12
    print("You're at least",days_in_years,"days old.")
    print("You,re at least",weeks_in_years,"weeks old.")
    print("You're at least",months_in_years,"months old.")

    #Makes a humorous statement
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter a adjective: ")
    place = input("Enter a place: ")
    print("Take your %s %s and %s it at the %s"%(adjective, noun, verb, place))

main()