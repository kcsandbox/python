# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # make opting to lower case and trim
    name = name.strip().lower()
    #print "[debug]: name_to_number: input-> ", name
    # convert name to number using if/elif/else
    if (name == 'rock'):
        return 0
    elif (name == 'spock'):
        return 1
    elif (name == 'paper'):
        return 2
    elif (name == 'lizard'):
        return 3
    elif (name == 'scissors'):
        return 4
    else:
        print "invalid choice. valid options :rock, spock, paper, lizard, scissors"
        return -1
    

def number_to_name(number):

    #print "[debug]: number_to_name: input->", number
    # convert name to number using if/elif/else
    if (number == 0):
        return 'rock'
    elif (number == 1):
        return 'Spock'
    elif (number == 2):
        return 'paper'
    elif (number == 3):
        return 'lizard'
    elif (number == 4):
        return 'scissors'
    else:
        print "invalid number. valid options :0, 1, 2, 3, 4"
        return 'atom-bomb'  #really? -- btw, it is dead code 
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    #print "[debug]--------- New Game ---------"
    # print out the message for the player's choice
    print "Player chooses ", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    #print "[debug]: player_number -> ", player_number
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    #print "[debug]: comp_number -> ", comp_number
    # convert comp_number to comp_choice using the function number_to_name()
    comp_name = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses ", comp_name
    # compute difference of comp_number and player_number modulo five
    difference = ((comp_number - player_number)) % 5
    # use if/elif/else to determine winner, print winner message
    if (difference == 0):
        print "Player and computer tie!" 
    elif (difference == 1):
        print "Computer wins!"
    elif (difference == 2):
        print "Computer wins!"
    elif (difference == 3):
        print "Player wins!"
    else :
        print "Player wins!"

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



