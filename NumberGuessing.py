import random
#Chosing a number
def choose():
    num = random.randint(1,30)
    return num
#prime checking
def prime(x):
    flag = False
    if x>1:
        for i in range(2,x):
            if x%i != 0:
                flag = True
            else:
                flag = False
                break
    return flag
def getguess():
    x = input("Enter an integer number \n")
    try:
        x = int(x)
        if x in range(1,31):
            return x
        else: return False
    except:
        return False
def greater_or_smaller(x,y):
    if x>y:
        print("Your number is larger")
    elif x<y:
        print("Your number is smaller")
#To check whether user has won or not
def win(x,y):
    if x==y:
        return True
def main():
    name = input("Enter your name:")
    print(name,"you have 8 chances to guess a number between 1 and 30")
    while True:
        count = 8
        num = choose()
        if prime(num) == True:
            print("The number is prime")
        else:
            print("The number is a composite number")
        while count != 0:
            print("Number of chances left",count)
            guess = getguess()
            if guess == False:
                print("Enter an integer number between 1 and 30")
                continue
            if win(guess,num):
                print("Congrats you've won\n")
                break
            greater_or_smaller(guess,num)
            count -= 1
            print()
        if count == 0:
            print("Bad luck",name,".The number was",num)
        a = input("Enter y or Y to play again\nOtherwise press whatever you want\t")
        if a.upper() != "Y":
            print("Goodbye")
            break
main()