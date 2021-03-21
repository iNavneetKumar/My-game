import turtle
print('Draw Any polygon')
t = turtle.Turtle()
n = int(input("Enter the no of the sides of the polygon from 3 to 10 : "))
l = 80
for i in range(n):
        turtle.forward(l)
        turtle.right(360 / n)

