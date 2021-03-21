def calculator_program():
    print('''What do you want to use in calculator
1.addition'
2.subtraction'
3.multiplication'
4.division
''')
    a = int(input('type the option number which you want to do:'))
    if a == 1:
        b = int(input('Enter the number of numbers you want the sum of:'))
        c = []
        for i in range (1,b+1):
            d = float(input('enter the number to add:'))
            c.append(d)
        print('The sum of the numbers', c , 'is' , sum(c))
    elif a == 2:
        b = float(input('enter the 1st no you want to subtract from:'))
        c = float(input('enter the 2nd no you want to subtract :'))
        print('The difference of number when we subtract',c,'from',b,'is', b-c)
    elif a == 3:
        b = float(input('enter the 1st No to multiply:'))
        c = float(input('enter the 2nd No to multiply:'))
        print('The product of number',b,'&',c,'is',b*c)
    elif a == 4:
        b = float(input('enter the value of divident or the no you want to divide:'))
        c = float(input('enter the value of divisor or the no you want to divide it with:'))
        print('the quotient when',b,'is divided from the no',c, 'is', b//c,'and the remainder is',b%c, 'and the final division is', b/c)
    else:
        print('the character or value you have entered is wrong')


while True:
    calculator_program()
    if(input("Do you want to use the calculator again Yes or No:")) in ["no","No"] :
        break
