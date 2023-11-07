import random

loss = 0
win = 0
toGame = True

print("Options: \n (1). Face \n (2). Crown")

while toGame:
    option = int(input("Choose you option: "))
    rand = round(random.random() * 100)
    if (rand % 2) == option:
        win += 1
        if option == 0:
            print("face, you win! \n")
        else:
            print("crown, you win! \n")
    else:
        loss += 1
        if option == 0:
            print("face, you loose! \n")
        else:
            print("crown, you loose! \n")

    message = input("Do you want to play again? (y/n):")

    if message == 'n':
        toGame = False

print("\n Final report:")
print("Number of games you have won " + str(win))
print("Number of games you have lost: " + str(loss))