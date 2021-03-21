def Simple_interest_and_compound_interest():
    print("Hey guys let's calculate simple and compount interest now")
    print('Now please enter the value asked below')
    p = float(input("Enter the amount(ptinciple):"))
    r = float(input("Enter the rate of interest:"))
    t = float(input("Enter the time period in years:"))
    x = p*(1+r/100)**t
    y = (p*r*t)/100
    print("The Compound interest is", x-p,"And the total amount to be paid is", x)
    print("The Simple interest is", y,"And the total amount to be paid is", y+p)
    if x > y:
       print("Compound interest", x-p, "is greater than", "simple interest", y)
    elif y > x:
         print("Simple Interest", y, "is greater than", "Compound interest", x-p)
    else :
         print ("The value you entered is wrong")
while True: 
    Simple_interest_and_compound_interest()
    if input("Do you want to calculate CI and SI again yes or no:") in ["no","No"]: 
        break
         



