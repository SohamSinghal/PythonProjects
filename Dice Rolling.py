import random
#To Choose the Number of Dice
def NumberOfDice():
    num = input("Enter number of dice you want to roll:")
    try:
        num = int(num)
        return num
    except:
        return False
#Using random function to get the number on dice
def NumberOnDice():
    num = random.randint(1,6)
    return num
def display(x):
    print("Number on dice is -",x)
#Main
def main():
    while True:
        if NumberOfDice != False:
            num_of_dice = NumberOfDice()
        else:
            print("Enter an integer please")
            continue
        dice = []
        while num_of_dice != 0:
            dice.append(NumberOnDice())
            num_of_dice -= 1
        for i in dice:
            display(i)
        cont = input("Press y or Y to rethrow the dice:")
        if cont.casefold()=="y":
            continue
        else:
            print("Goodbye")
            break
main()