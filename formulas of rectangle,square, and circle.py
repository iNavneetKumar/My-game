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
