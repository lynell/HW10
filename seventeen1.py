def seventeen():
    marbles = 17
    print "Number of marbles left in the jar: 17"
    while (marbles>=0):
        try:
            
            user_ip = int(raw_input("Your turn: How many marbles will you remove (1-3)?"))
            
        except:
            print "Invalid Input"
            continue
        else:
            if user_ip<1 or user_ip>3:
                print "Sorry, that is not a valid option. Try again!"
                continue
            else:
                pass
            if (marbles - user_ip) > 0:
                marbles -= user_ip #marbles removed by user
                print "Number of marbles left: " + str(marbles)
            else :
                print "You lose"
                break
            
            print "Computer's turn..."
            
            if (marbles - user_ip) > 0:
                print "Computer removed " + str(user_ip) +  " marbles." 
                marbles -= user_ip #marbles removed by user
                print "Number of marbles left in the jar: " + str(marbles)
            else :
                print "You win"
                break
def main():
    print "Let's play the game of Seventeen!"
    seventeen()


main()
