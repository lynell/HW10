def seventeen(game):
    marbles = 17
    winner = ""
    seq = ""
    for i in game:
        try:
            i = int(i)
        except:
            continue
        else:
            if i<1 or i>3:
                continue
            else:
                pass
            if (marbles - i) > 0:
                marbles -= i #marbles removed by user
                seq += "-" + str(i)
                
            else :
                winner = "P2"
                return [seq,winner]
            
            if (marbles - i) > 0:
                marbles -= i #marbles removed by user
                seq += "-" + str(i)
            else :
                winner = "P1"
                return [seq,winner]
def main():
    print "Let's play the game of Seventeen!"
    game_number = 1
    with open("final.txt","a") as fwrite:
        with open("i206_placein_input_0.txt","r") as fin:
            for line in fin:
                game_number+= 1
                line = line.strip()
                game = line.split(",")
                seq = seventeen(game)
                fwrite.write("Game #" +str(game_number) + ". Play Sequence : "  + seq[0][1:] + ". Winner: " + seq[1] + '\n')
            
    

main()
