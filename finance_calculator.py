#**********************Pseudocode********************
#Add the import math built-in function
#print out the a message, that will pop out the moment the user opens the application
#the message should say : Investment - to calculate the amount of interest you'll earn on your investment
#                       : Bond - to calculate the amount you'll have to pay on a home loan
#create a string calculation_option to store, which calculation the user want
#ask the user to enter which calculation they want, put in these following word :
# "Enter either "Investment" or "Bond from the menu above to proceed:"
#using the if,elif and else statement with "OR", "AND" and "!" determine which action to take and uppercase and lowercase should not affect the answer
#if the user wants "investment", create three float variable => amount, interest_rate and r and one integer variable => year
#ask the user to enter the values of : the amount they want to invest => stored in amount, the number of years they want to invest => stored in years
# the interest rate => stored in interest_rate and r will be calculates as => r = interest_rate/100
#Create a string variable that will require the user to choose which type of investment they want( simple or compound investment rate)
#calculate the amount they will gain and print it out
# if the user wants a bond calculation, ask the user to enter house value => integer house_value, already existing float variable interest_rate and a integer variable months =>> will store number of months to pay the bond
#calculate i with is i= (interest_rate/100)/(12)
#calculate the amount they will pay back and print it out

import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("")
calculation_option = input("'Investment' or 'Bond' from the menu above to proceed: ")
# printing out the first thing the user will see and asking for their imput

investment_option1 = "investment"
investment_option2 = "INVESTMENT"
investment_option3 = "Investment"
bond_option1 = "BOND"
bond_option2 = "Bond"
bond_option3 = "bond"
#you do not have to declare these values, as you will see in getting the investment_type variable below 
if (calculation_option == investment_option1) or (calculation_option == investment_option2) or (calculation_option == investment_option3) :
    amount = float(input("Please enter the amount you wish to invest: "))
    interest_rate = float(input("Please enter the interest rate: "))
    year = int(input("Please enter the number of years you wish to invest: "))
    #asking for the user to enter the amount, rate and years they want to invest for
    r = interest_rate/100
    #calculating the interest rate, in how they calculate it in mathematics
    print("Please select which investment would you like: ")
    #asking the user the type of invest they want.
    investment_type = input("'Simple' rate or 'Compound' rate " )
    if (investment_type == 'simple') or (investment_type =="Simple" or (investment_type == "SIMPLE")) :
        a = amount * (1+ r * year) #calculation for simple rate invest
        print(f"The total amount that you will get for a simple rate investment after {year} years is : {round(a, 2)}")
    elif (investment_type == 'Compound') or (investment_type =="COMPOUND" or (investment_type == "compound")) :
        a = amount * math.pow((1+r),year) # calculations for compound rate invest 
        print(f"The total amount that you will get for a simple rate investment after {year} years is : {round(a, 2)}")
    else :
        print("You've inserted an invalid option!")
        # used the if, elif and else statement to give the correct answer depending on the invest they want
elif (calculation_option == bond_option1) or (calculation_option == bond_option2) or (calculation_option == bond_option3) : 
    house_value = int(input("Please enter the value of the house, you wish to buy: "))
    interest_rate = float(input("Please enter the interest rate: "))
    months = int(input("Please enter the number of months you wish to payment back the home loan: "))
    i = (interest_rate /100) / 12 #calculating the interest rate for bond, like how its done in finance
    repayment = (i * house_value) /(1-(1 + i)**(-months)) #calculating the amount the user will have to pay each month for the bond
    print(f"The amount that you will payback each month is : {round(repayment, 2)}")
else :
    print("You have entered an invalid option")
    #used a if, elif and else statement for when the user choose that they want th application to do for them, investment calculation or bond
