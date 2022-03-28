import math
print("Project Task 12 ")
#formula clearification is as follows
#P = amount the user entered
#r = interest entered devided by 100
#t = number of years the money being invested
#A = total amount once the interest has been paid
#--------------------------------------------------------------------------

calculator = input("chose calculator method : investment or home_loan or bond : ") #user selecting the calculations to do 
#calculating/entering the results of selected method 
if calculator == "investment":
    amount = int(input("Enter amount to deposit : "))
    percentage = float(input("Enter percentage : "))
    years = int(input("Enter number of years to invest : "))
    interest = input("Investment type ?  compound or simple : ")
    if interest == "simple" :
#given formula used for simple investment calculations
#A =P*(1+r*t)

#formula and its values       
        A = amount * (1 + years * percentage)
        print(A)
    else:
        interest  == "compound"
#formula used for compund interest calculations
        A = amount * math.pow((1 + years), percentage)
        print(A)
elif calculator == "home_loan":
    amount = int(input("Enter amount to deposit : "))
    percentage = float(input("Enter percentage : "))
    years = int(input("Enter number of years to invest : "))
    interest = input("Investment type ?  compound or simple : ")
    if interest == "simple":
        A = amount * (1 + years * percentage)
        print(A)
    else: 
        interest =="compound"
        A = amount * math.pow((1 + years), percentage)
        print(A)
        
#calculating bond
elif calculator == "bond":
    value_of_house = float(input("Enter value of the house : "))
    bond_interest = float(input("Enter bond interest : "))
    months_to_pay = int(input("Enter months to pay : "))
#when calculating bond 
#P = is the present value of the house "named" variable (value_of_house)
#i =  is the anual interest rate, calculated by dividing the annual rate by 12 named "bond_interest variable"
#n = is the number of months over which the bond will be repaid named "months_to_pay"
# x =  money the user will have to repay each named repay_ammount
#---------------------------------------------------------------------------------------------
#calculating the money the user is going to repay
#  #formula
    repay_amount = ((bond_interest / 12) * value_of_house) / (1 - (1+ value_of_house) ** (-bond_interest / 12)) #correction formula
    print(repay_amount)
else:
    print("invalid input")
