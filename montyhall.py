from random import randint
from random import choice

def montyhall(playerchoice):
    prize = randint(1,3)
    if (prize == 1):
        noluck1 = randint(2,3)
        if (noluck1 == 2):
            noluck2 = 3
        else:
            noluck2 = 2
    if (prize == 2):
        noluck1 = choice([1,3])
        if (noluck1 == 1):
            noluck2 = 3
        else:
            noluck2 = 1
    if (prize == 3):
        noluck1 = randint(1,2)
        if (noluck1 == 1):
            noluck2 = 2
        else:
            noluck2 = 1
            
    "out of the two remaining doors, pick the one that does not have\
    prize behind"
    if (playerchoice == prize):
        openeddoor = choice([noluck1, noluck2])
    if (playerchoice == noluck1):
        openeddoor = noluck2
    else:
        openeddoor = noluck1
    

    newplayerchoice = [i for i in [1,2,3] if (i != playerchoice and
                                                i != openeddoor)][0]
        
    win = (newplayerchoice == prize)
    return win

def test(num):
    wincount = 0
    newnum = num
    for i in range(1,num+1):
        pchoice = randint(1,3)
        print("Trial #" + str(i))
        i += 1
        win = montyhall(pchoice)
        if (win == True):
            wincount += 1
            print("Win!")
        if (win == False):
            print("Lose.")
        print("-----------")
    print("By swapping, we won " + str(wincount) + " times in " + str(newnum)\
          + " trials.")
    print("The possibility of Winning = " + "%.2f" % (wincount/num*100) + "%.\n")
    repeat = input("Please enter:\n" + "'y' to try again\n" +
                   "'c' to change the number of trials\n" +
                   "'n' to stop\n")
    while (repeat != "n" and repeat != "N"):
        if (repeat == "y" or repeat == "Y"):
            test(num)
            repeat = "n"
        if (repeat == "c" or repeat == "C"):
            newnum = int(input("Number of trials = "))
            test(newnum)
            repeat = "n"
        else:
            repeat = input("Please enter the correct value. (y/n/c)")
    return

def init():
    num = int(input("Please enter the number of trials you want to take: "))
    return test(num)

init()
