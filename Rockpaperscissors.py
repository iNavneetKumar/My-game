from random import randint
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
