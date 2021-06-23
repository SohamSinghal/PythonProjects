import random
#Generate a list
def GenerateList():
    list = random.sample(range(1,101),50)
    return list
#Get a number ranging from 1 to 100 from user
def GetNumber():
    num = input()
    try:
        num = int(num)
        return num
    except:
        return False
#Do binary search
def BinarySearch(list,start,last,num):
	if last >= start:
		mid = (last + start) // 2
		if list[mid] == num:
			return mid
		elif list[mid] > num:
			return BinarySearch(list, start, mid - 1, num)
		else:
			return BinarySearch(list, mid + 1, last, num)
	else:
		return -1
#Main
def main():
    list = GenerateList()
    print("Enter a number you'd like to search from a list of 50 random number ranging from 1 to 100")
    x = GetNumber()
    print(type(x))
    if x == False or x not in range(1,101):
        print("Number wasn't a integer between 1 and 100")
        return
    else:
        found = BinarySearch(list,0,len(list)-1,x)
    if found == None:
        print("Number not in list")
    else:
        print("Number found at",found+1)

main()