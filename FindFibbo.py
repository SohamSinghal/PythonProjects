#Get number from user
def GetNumber():
    print("Enter an integer number you'd like to check")
    a = input()
    try:
        a = int(a)
        if a>0:
            return a
        else:
            return -1
    except:
        return -1
#Check in fibonacci Series
#0 1 1 2 3 5 8 13
def CheckInFibo(x):
    found = False
    a,b,c = 0,1,1
    while c<=x:
        a,b = b,c
        c = a+b
        if c == x:
            found = True
            break
    return found
#Give some message
def message(found):
    if found == True:
        print("Number exists in fibonacci series")
    else:
        print("Number does not exist in fibonacci series")
#Main
def main():
    while True:
        num = GetNumber()
        if num == -1:
            print("Invalid Number")
        else:
            f = CheckInFibo(num)
            message(f)
        print("Press \"y\" to check for another number.")
        again = input()
        if again.casefold() != "y":
            print("Goodbye")
            break
main()
