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
   	# Check base case
	if last >= start:

		mid = (last + start) // 2

		# If element is present at the middle itself
		if list[mid] == num:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left sublistay
		elif list[mid] > num:
			return BinarySearch(list, start, mid - 1, num)

		# Else the element can only be present in right sublistay
		else:
			return BinarySearch(list, mid + 1, last, num)

	else:
		# Element is not present in the array
		return -1
#Main
def main():
    list = [1,2,3,4,5,6,7,8,9]
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