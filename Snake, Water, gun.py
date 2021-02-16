# Snake , water , gun!

import random

computer_points = 0
your_points = 0
num_of_chances = 10

print("Please Enter your name to get started!")
name1 = str(input())
print("Enter Your Computer's name")
name2 = str(input())
while(True):
    print("Welcome to SNAKE , WATER , GUN GAME!\n")
    num_of_chances = num_of_chances - 1
    print("Please type S for Snake, W for Water, and G for Gun")
    print(f"Number of chances left:{num_of_chances} out of 10")
    if num_of_chances == 0:
        print("The number of chances have finished")
        print(f"You got {your_points} points")
        print(f"The computer got {computer_points} points")
        if your_points > computer_points:
            print("You won the game!", f"And its sad that the {name2} loose :(")
        else:
            print(f"The computer won the game! , and its sad that {name1} loose :(")
            break

    toss1 = str(input())
    if toss1 == "S":
        list1 = ["S" , "W" , "G"]
        choice1 = random.choice(list1)
        print("You chose :", toss1 )
        print("And your computer chose:", choice1)
        if choice1 == "S":
            print("Its a tie and both of you get 0 points")
            print(f"Number of points you have:{your_points}")
            print(f"Number of points the computer has:{computer_points}")
            continue

        if choice1 == "W":
            print("Your snake drank all the water and bit the computer with his venomous bite!")
            your_points = your_points + 1
            print(f"Number of points you have:{your_points}")
            print(f"Number of points the computer has:{computer_points}")
            continue

        if choice1 == "G":
            print("The computer shot your snake with his powerful gun! ")
            print(f"Number of points you have:{your_points}")
            computer_points = computer_points + 1
            print(f"Number of points the computer has:{computer_points}")
            continue


    elif toss1 == "W":
        list2 = ["S" , "W" , "G"]
        choice2 = random.choice(list2)
        print("You chose :", toss1)
        print("And your computer chose:", choice2)
        if choice2 == "S":
            print("The computer's snake drank all the water and bit you with his venomous bite!")
            print(f"Number of points you have:{your_points}")
            computer_points = computer_points + 1
            print(f"Number of points the computer has:{computer_points}")
            continue

        if choice2 == "W":
            print("Its a tie and both of you get 0 points!")
            print("Number of points you have:", your_points)
            print("Number of points the computer has:", computer_points)
            continue

        if choice2 == "G":
            print("The water stopped the striking bullet hitting you!")
            your_points = your_points + 1
            print("Number of points you have:", your_points)
            print("Number of points the computer has:", computer_points)
            continue


    elif toss1 == "G":
        list3 = ["S", "W", "G"]
        choice3 = random.choice(list3)
        print("You chose :", toss1)
        print("And your computer chose:", choice3)
        if choice3 == "S":
            print("Your powerful gun shot the snake with a headshot!")
            your_points = your_points + 1
            print("Number of points you have:", your_points)
            print("Number of points the computer has:", computer_points)
            continue

        if choice3 == "W":
            print("The computer's water stopped your bullet entering the system!")
            print("Number of points you have:", your_points)
            computer_points = computer_points + 1
            print("Number of points the computer has:", computer_points)
            continue

        if choice3 == "G":
            print("Its a tie and both of you get 0 points!")
            print("Number of points you have:", your_points)
            print("Number of points the computer has:", computer_points)
            continue







