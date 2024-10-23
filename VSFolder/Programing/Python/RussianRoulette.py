import random
def RR(x = 1):
    list1 = [1,2,3,4,5,6]
    list2 = [1,2,3,4,5]
    list3 = [1,2,3,4]
    list4 = [1,2,3]
    list5 = [1,2]
    list6 = [1]
    if x == 1:
        num1 = random.choice(list1)
    elif x == 2:
        num1 = random.choice(list2)
    elif x == 3:
        num1 = random.choice(list3)
    elif x == 4:
        num1 = random.choice(list4)
    elif x == 5:
        num1 = random.choice(list5)
    elif x == 6:
        num1 = random.choice(list6)
    if num1 == 1:
        return(False)
    else:
        return(True)
another = True
play1 = input("Would you like to play Y or N: ")
print("Ok")
banana = 1
while True:
    if play1 == "y" or play1 == "Y":
        while another == True:
            hi = RR(banana)
            banana = banana + 1
            if hi == True:
                again = input("You live would you like to play again: ")
                if again == "n" or again == "N":
                    while True:
                        print("Lame")
                else:
                    print("Ok")
            else:
                print("You DIE")
                another = False
    else:
        print("Lame")