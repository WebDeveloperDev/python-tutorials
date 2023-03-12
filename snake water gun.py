print("Welcome to snake Water Gun game")
print("Game instruction: \n 1. Players should select any one among Snake Water and Gun \n 2. Don't feel unluckey because its just a random choise taken by computer")
chance=10
boot=0
opponent=0
while(chance>0):
    userch=input("Type S for snake ,W for water and G for gun\n")
    def bootfunk():
        import random
        li=["S","W","G"]
        return random.choice(li)
    bootch=bootfunk()
    print(bootch)
    if userch.capitalize()==bootch:
        print("drow")
    elif userch.capitalize()=="S" and bootch=="W":
        print("You win, snake drunk the water")
        opponent+=1
    elif userch.capitalize()=="S" and bootch=="G":
        print("you lost, Snake is killed by Gun")
        boot+=1
    elif userch.capitalize()=="W" and bootch=="S":
        print("You lost, water is drunk by snake")
        boot += 1
    elif userch.capitalize() == "W" and bootch == "G":
        print("You win, gun is sank in the water")
        opponent += 1
    elif userch.capitalize() == "G" and bootch == "S":
        print("You win , snake is killed by your gun")
        opponent += 1
    elif userch.capitalize() == "G" and bootch == "W":
        print("You lost ,your gun is sank in water ")
        boot += 1
    else:
        print("Read the instructions given")
    chance-=1
    print(f"{chance} chances is left")
print("Game over")
print(f"Your score is {opponent} \nboot score is {boot}")

