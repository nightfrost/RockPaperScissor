#Rock, paper, scissor by Lucas :) https://github.com/nightfrost
#This is only made for small practice.
from random import randint

def user_input(): #I get the user input and assign a string value
    x = input("Please make your choice...\nRock = 1\nPaper = 2\nScissor = 3\n")
    if x == 1:
	    print "You picked Rock."
	    return "Rock"
    elif x == 2:
	    print "You picked Paper"
	    return "Paper"
    elif x == 3:
	    print "You picked Scissor"
	    return "Scissor"
    else:
	    print "\n\n\nYou picked a number that is not valid.\nPlease try again.\n"

def machine_input(): #Randomly generates a number and assigns a string value
    x = machine_choice = randint(1,3)
    if x == 1:
	    return "Rock"
    elif x == 2:
	    return "Paper"
    elif x == 3:
	    return "Scissor"

def who_wins(): #Decides who wins.
    if user_choice == machine_choice:
        print "It's a tie. Gasp! You both picked %s" %user_choice
        return
    if user_choice == "Rock":
        if machine_choice == "Paper":
            print "Machine picked %s, you lose..." %machine_choice
        else:
            print "You win! Machine picked %s" %machine_choice
    elif user_choice == "Paper":
        if machine_choice == "Scissor":
            print "Machine picked %s, you lose..." %machine_choice
        else:
            print "You win! Machine picked %s" %machine_choice
    elif user_choice == "Scissor":
        if machine_choice == "Rock":
            print "Machine picked %s, you lose..." %machine_choice
        else:
            print "You win! Machine picked %s" %machine_choice

user_choice = user_input()
machine_choice = machine_input()
who_wins()