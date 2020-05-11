#Final Project
# I, Phan, Truong Son, 000824388, certify that all code submitted is my own work; that I have not copied it from any other source.  I also certify that I have not allowed my work to be copied by others.

import random

def rollDie(faces):
    # module to roll a single die with a variable number of faces
    # ASSUME faces is a valid positive integer, greater than 1
    rollingDice = random.randint(1, int(faces))
    return rollingDice

def average(inList):
    # ASSUME inList is a list of numbers and the length of inList is > 0
    sumNumber = 0
    for i in inList:
        sumNumber += i
    avg = round(sumNumber / len(inList))
    return avg

def calculatePercentage(sides,dice,diceRolls):
    # ASSUME sides*dice != 0, sides, dice are numbers
    # ASSUME diceRolls is a list of numbers
    maxScore = int(sides)*int(dice)
    sumNumber = 0
    for i in diceRolls:
        sumNumber += i
    percentage = sumNumber/maxScore
    return percentage

def isPrime(number,sides,dices):
    # ASSUME number,sides,dices is an integer
    # Check the number is prime and maximum score >=20
    notPrime = [1,2,4,6,8,9,10,12,14,15,16,18,20]
    if number in notPrime or int(sides)*int(dices)<20:
        return False
    return True

def pattern1(sides,dice):
    # ASSUME sides > 0 and dice is a list of integers
    # Check all dices have same value
    result = all(i == dice[0] for i in dice)
    if int(sides) >= 4 and result:
        return True
    return False


def pattern3(dices,dice):
    # ASSUME dices is an integers
    # ASSUME dice is a list of integers
    # Check half the dice are grater than or equal rounded average
    avgNumber = average(dice)
    count= 0
    for i in dice:
        if i >avgNumber:
            count += 1
    if int(dices) >= 5 and count>= (len(dice)/2):
        return True
    return False

def pattern4(sides,dices,dice):
    # ASSUME dice is a list of integers
    # ASSUME sides, dices are integers
    # Check all the dice are different
    for i in range(0,len(dice) -1):
        for j in range(i+1, len(dice)):
            if dice[i]== dice[j]:
                valid = "False"
            else:
                valid="True"
    if int(sides) > int(dices) and int(dices) > 4 and valid == "True":
        return True
    return False
        

def pattern5(number,sides,dices,dice):
    
    # ASSUME dice is a list of integers
    # ASSUME number, sides, dices are integers
    # Check no pattern matches
    if isPrime(number,sides,dices) and pattern1( sides, dice ) and\
       pattern3( sides,dice) and not pattern4( sides,dices, dice ):
        return True
    return False
        
def bonusFactor(number,sides,dices,dice):
    # ASSUME dice is a list of numbers
    # ASSUME number,sides, dices are integers
    bonus = 0
    if isPrime( number,sides, dices ):
        bonus= bonus + 15
    if pattern1( sides, dice ):
        bonus = bonus + 10
    if pattern3( dices, dice):
        bonus = bonus + 5
    if pattern4( sides,dices, dice ):
        bonus = bonus + 8
    if pattern5( number,sides,dices, dice ):
        bonus = bonus + 1
    return bonus


def score(sides,dices,diceRolled,bonus):
    # ASSUME sides and dices are integers > 0
    # ASSUME diceRolled is a list of integers
    percentage=calculatePercentage(sides,dices,diceRolled)
    userScore = percentage * bonus + 824388%2020
    return userScore


# main

# Don't forget a statement of authorship at the top of the file!

print("COMP 10001 - W2020 Final Project by Truong Son Phan, Student number 000123456.")
print("Welcome to my dice game, good luck!")

yes = ["yes", "YES", "Yes", "yEs", "yeS", "YEs", "YeS", "yES"]
no = ["No", "no", "nO", "NO"]
playAgain = "Yes"
turns=0
listOfScore = [ ]

while playAgain in yes:
    #Get user INPUT
    faces = input("Enter # of faces [2,20]: ")
    while not (faces.isdigit() and  int(faces) >=2 and int(faces) <= 20):
        print("I'm sorry, that isn't a valid positive integer, please try again.")
        faces = input("Enter # of faces[2,20]: ")

    dices = input("Enter # of dice [3,6]: ")
    while not (dices.isdigit() and int(dices)>=3  and int(dices)<=6):
        print("I'm sorry, that isn't a valid positive integer, please try again.")
        dices = input("Enter # of dice [3,6]: ")

    maximumScore= int(faces)*int(faces)

    #Creat User dice list
    diceCounter = 1
    diceList = []

    while diceCounter <= int(dices):
        diceRoll = rollDie(faces)
        diceList = diceList + [diceRoll]
        diceCounter += 1
    
    print("You have rolled: " + str(diceList))


    #Show user die sum and average
    sumNumber = 0
    for i in diceList:
        sumNumber += i
    
    averageNum = average(diceList)
    print("These die sum to " + str(sumNumber) + " and have an average rounded \
value of " + str(averageNum) + ".")


    #Show user patterns

    if pattern1(faces,diceList):
        print("Pattern 1 matched, you have rolled: " + str(diceList))
    else:
        print("Patter 1 not matched, you have rolled: " + str(diceList))

    if isPrime(sumNumber,faces,dices):
        print("Pattern 2 matched, " + str(sumNumber) + " is a prime \
number and maximum score "+ str(maximumScore)+ " is greater than or equal to 20")
    else:
        print("Pattern 2 not matched, " + str(sumNumber) + " is not a \
prime number or maximum score "+ str(maximumScore)+ " is less than 20")

    if pattern3(dices,diceList):
        print("Pattern 3 matched, more than half of " + str(diceList) + "\
are greater than or equal to the average of " + str(averageNum)+ ".")
    else:
        print("Pattern 3 not matched, less than " + str(diceList) + " are \
greater than or equal to the average of " + str(averageNum)+ ".")

    if pattern4(faces,dices,diceList):
        print("Pattern 4 matched , all the value in " + str(diceList) +"\
are different and die faces > total dice > 4.")
    else:
        print("Pattern 4 not matched , all the value in " + str(diceList) +"\
are not different or die faces= < total dice =< 4.")

    if pattern5(sumNumber,faces,dices,diceList):
        print("Pattern 5 matched, because none of the pattern above matched.")
    else:
        print("Pattern 5 not matched, because some of the patterns above matched.")


    # Calculate bonus and score
    totalBonus = bonusFactor(sumNumber,faces,dices,diceList)
    print("Your bonus factor is: " + str(totalBonus) + ".")
    totalScore = score(faces,dices,diceList,totalBonus)
    print("These dice are worth: " + str(round(totalScore)) + ".")

    #Ask user to reroll

    userInp = input("Do you want to reroll any dice?('yes','no'): ")
    while not(userInp in yes or userInp in no):
        userInp = input("Im sorry, the choices are ('yes','no'): " )
    
    if userInp in yes:
        reRollCounter = 1
        listInd= 0
        for i in diceList:   
            reRoll= input("Reroll die " +str(reRollCounter) +"\
(was " + str(diceList[listInd]) + "('yes','no'))")
            while not(reRoll in yes or reRoll in no):
                reRoll = input("Im sorry, the choices are ('yes','no'): " )
            if reRoll in yes:
                diceList[listInd] = random.randint(1, int(faces))
            else:
                i = i
            reRollCounter += 1
            listInd  += 1
        print("You have rolled: " + str(diceList))

        sumNumber = 0
        for i in diceList:
            sumNumber += i
    
        averageNum = average(diceList)
        print("These die sum to " + str(sumNumber) + " and have an average rounded \
value of " + str(averageNum))    
      
        if pattern1(faces,diceList):
            print("Pattern 1 matched, you have rolled: " + str(diceList))
        else:
            print("Patter 1 not matched, you have rolled: " + str(diceList))

        if isPrime(sumNumber,faces,dices):
            print("Pattern 2 matched, " + str(sumNumber) + " is a prime number and \
maximum score "+ str(maximumScore)+ " is greater than or equal to 20")
        else:
            print("Pattern 2 not matched, " + str(sumNumber) + " is not a prime number or\
 maximum score "+ str(maximumScore)+ " is less than 20")

        if pattern3(dices,diceList):
            print("Pattern 3 matched, more than half of " + str(diceList) + " are \
greater than or equal to the average of " + str(averageNum)+ ".")
        else:
            print("Pattern 3 not matched, less than " + str(diceList) + " are \
greater than or equal to the average of " + str(averageNum)+ ".")

        if pattern4(faces,dices,diceList):
            print("Pattern 4 matched , all the value in " + str(diceList) +" are \
different and die faces > total dice > 4.")
        else:
            print("Pattern 4 not matched , all the value in " + str(diceList) +" are \
not different or die faces= < total dice =< 4.")

        if pattern5(sumNumber,faces,dices,diceList):
            print("Pattern 5 matched, because none of the pattern above matched.")
        else:
            print("Pattern 5 not matched, because some of the patterns above matched.") 

        totalBonus = bonusFactor(sumNumber,faces,dices,diceList)
        print("Your bonus factor is: " + str(totalBonus) + ".")
        totalScore = score(faces,dices,diceList,totalBonus)
        print("These dice are worth: " + str(round(totalScore)) + ".")

    turns += 1
    listOfScore=[] + [round(totalScore)]
    
    playAgain = input("Do you want to play again: ")
    while not(playAgain in yes or playAgain in no):
        playAgain = input("Im sorry, the choices are ('yes','no'): " )

avgListScore = round(average(listOfScore))
print("Today you have played " + str(turns) + " with an average score of " \
      + str(avgListScore) + ".")




    
