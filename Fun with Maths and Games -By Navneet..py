def Fun_with_Maths_And_Games():
    import time
    import turtle
    from random import randint
    print("Fun with Maths And games")
    print("so let do some exciting thing")
    #This program is basically a combination of many programs.
    time.sleep(1.2)
    print("coundown begin")
    for i in range(3,0,-1):
        time.sleep(1.2)
        print(i)
    print('lets begin')
    print('''You can select the options you want to do
1.Draw a polygon
2.Play a maths quiz
3.Play rock paper scissors
4.calculator
5.calculate simple and compound interests
6.formulas of rectangle, square and circle.''')
    j = int(input('Select the number of the choice from the list above:-'))
    if j == 1 :
        print('''Draw Any polygon
And remember after typing the number of sides you want please check the other,
turtle tab Which will show you your required polygon.''')
        t = turtle.Turtle()
        n = int(input("Enter the no of the sides of the polygon from 3 to 10 : "))
        l = 80
        for i in range(n):
            turtle.forward(l)
            turtle.right(360 / n)

    if j == 2:
        def maths_quiz():
            print('---------------------------------------------------------')
            print('''hello and welcome to the quiz
Here we will ask you some questions related to mathematics''')
            input('So if you are ready press enter')
            print('''Question 1.
If 1=3

2=3

3=5

4=4

5=4
''')
            a = ('you get a point,')
            b = 0
            c = ('Your answer is correct,')
            d = ('your current score is: ')
            e = ('your answer is incorrect,')
            p = int(input('Then, 6=?: '))
            if p == 3:
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '6 = 3, because ‘six’ has three letters', d, b)

            print('''--------------------------------------------------------------------
Question 2

There are 50 dogs signed up for a dog show,

consisting of large and small dogs.

There are 36 more small dogs than large dogs.

''')
            q = int(input('Then, How many small dogs have signed up to compete? :'))
            if q == 43:
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
To figure out how many small dogs are competing,
you have to subtract 36 from 50 and then divide that answer, 14 by 2,
to get 7 dogs, or the number of big dogs competing.
But you’re not done yet!You then have to add 7 to 36 to get
the number of small dogs competing, which is 43.''', d, b)

            print('''--------------------------------------------------------------------
Question 3
[16][06][68][88][?][98]
''')
            r = int(input('What is the number of empty space covered by the question mark[?] ? :'))
            if r == 87:
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
If you flip the image upside down,
you’ll see that what you’re dealing with is a simple number sequence.
[86][?][88][89][90][91]''', d, b)

            print('''--------------------------------------------------------------------
Question 4

I am an odd number. Take away one letter and I become 'even' .

''')
            s = input(' What number am I ? :')
            if s in ['7', 'seven', 'Seven'] :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
Seven (take away the ‘s’ and it becomes ‘even’).''', d, b)

            print('''--------------------------------------------------------------------
Question 5

Sally is 54 years old and her mother is 80.

''')
            t = int(input(' how many years ago was Sally’s mother 3 times her age? :'))
            if t == 41 :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
41 years ago, when Sally was 13 and her mother was 39.''', d, b)

            print('''--------------------------------------------------------------------
Question 6
There is a three-digit number.
The second digit is four times as big as the third digit,
while the first digit is three less than the second digit.
''')
            u = int(input(' What is the number? :'))
            if u == 141 :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
The answer is 141, The second digit 4 is four times as big as the third digit 1,
while the first digit 1 is three less than the second digit 4.''', d, b)

            print('''--------------------------------------------------------------------
Question 7

Solve:-
-15 + (-5x) = 0
''')
            v = int(input(' What is the value of x? :- '))
            if v == -3 :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
The answer is -3. As we bring -15 to rhs it becomes 15 so the eq is -5x = 15
now bringing -5 from x to rhs it becomes 15/-5 so when we equate it we het -3.
''', d, b)

            print('''--------------------------------------------------------------------
Question 8

A man is climbing up a mountain which is inclined.
He has to travel 100 km to reach the top of the mountain.
Every day He climbs up 2 km forward in the day time.
Exhausted, he then takes rest there at night time.
At night, while he is asleep, he slips down 1 km backwards because the mountain is inclined.
''')
            w = int(input(' Then how many days does it take him to reach the mountain top?  :- '))
            if w == 99 :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
The answer is 99. As we can see he climbs 2km and falls down 1 km everyday.
so till 98 days he will climb 98 km (98 days *1 km). so on the 99th day,
he climbs 2 km more which is equal to 98 + 2 = 100km so he climbs it in 99 days.
''', d, b)

            print('''--------------------------------------------------------------------
Question 9

If 1 = 4

2 = 16

3 = 64

''')
            x = int(input(' What is the value of 4 = ? :- '))
            if x == 256 :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
as we can see

4**1 or 4^1 = 4

4**2 or 4^2 = 16

4**3 or 4^3 = 64

4**4 or 4^4 = 256
''', d, b)

            print('''--------------------------------------------------------------------
Question 10

Look at this series: 36, 34, 30, 28, 24, …

''')
            y = int(input(' What number should come next? :- '))
            if y == 22 :
                b = b + 1
                print(c, a , d, b)
            else:
                print(e, '''
as we can see
36,36 - 2 = 34,34 - 4 = 30, 30 - 2 = 28, 28 - 4 = 24, so next will be 24 - 2 =22.
''', d, b)
            print('--------------------------------------------------------------------')
            print("So that's it thanks for playing the quiz.you got", b,"Out of 10.")
            print('--------------------------------------------------------------------')

            
        while True:
            maths_quiz()
            if(input("Do you want to play the same quiz again Yes or No:")) in ["no" , "No"]:
                break

    if j == 3:
        print('''Hey guys here lets play rock paper Scissors.
You(Player) Vs Me(Computer/Navneet)
Let the battle Begin ^_^!!
''')
        x = input('What is your name :- ')
        def rock_paper_scissors():
            t = ["Rock", "Paper", "Scissors"]
            computer = t[randint(0,2)]
            player = input("Rock, Paper, Scissors?")
            if player == computer:
                print("Tie!")
            elif player == "Rock":
                if computer == "Paper":
                    print(x," lose!", computer, "covers", player)
                else:
                    print(x," win!", player, "smashes", computer)
            elif player == "Paper":
                if computer == "Scissors":
                    print(x," lose!", computer, "cut", player)
                else:
                    print(x," win!", player, "covers", computer)
            elif player == "Scissors":
                if computer == "Rock":
                    print(x," lose!", computer, "smashes", player)
                else:
                    print(x," win!", player, "cut", computer)
            else:
                print("That's not a valid play. Check your spelling!")
        while True:
            rock_paper_scissors()
            if(input("Do you want to play again Yes or No:")) in ["no","No"] :
                break

    if j == 4:
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

    if j == 5:
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


    if j == 6:
        def Formulas_Of_Square_Rectangle_Circle():
            print('''Hello guys now in this part we will calculate different
formulas like some basic formula of 3 different shapes
which are Square, Rectangle and Circle.

So here you just have to enter 3 values and those are
length(l),breadth(b) and radius(r). That's it.

So lets begin :)
''')
            l = int(input("Enter a value for length ="))
            b = int(input("Enter a value for breadth ="))
            r = int(input("Enter a value for radius ="))
            a = ('Area of a rectangle=', l*b)
            b = ('perimeter of a rectangle', 2*(l+b))
            c = ('Area of a square=', l*l)
            d = ('Perimeter of a square=', 4*l)
            e = ('Diameter=', r*2)
            f = ('Area of Circle=', 22/7*r**2)
            g = ('Circumference of Circle=', 2*22/7*r)
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            print(g)
        while True:
            Formulas_Of_Square_Rectangle_Circle()
            if(input("Do you want to find the values again Yes or No:")) in ["no" , "No"]:
                break

        
        

while True:
    Fun_with_Maths_And_Games()
    if(input("Do you want to Run Fun with maths and games again Yes or No:")) in ["no" , "No"]:
        break
