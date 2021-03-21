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

