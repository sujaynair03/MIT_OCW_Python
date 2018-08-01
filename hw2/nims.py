# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):
    while [pile > 0]:
        player_1m=raw_input("make a move: ")
        player_1m = int(player_1m)
        while not ((player_1m > 0) and (player_1m <= max_stones)):
            player_1m = int(raw_input("make a valid move: "))
        pile = pile - player_1m
        if pile < max_stones:
            max_stones = pile
        print pile
        if pile == 0:
            return "player_1 wins"

        player_2m=raw_input("make a move: ")
        player_2m = int(player_2m)
        while not ((player_2m > 0) and (player_2m <= max_stones)):
            player_2m = int(raw_input("make a valid move: "))
        pile = pile - player_2m
        if pile < max_stones:
            max_stones = pile
        print pile
        if pile == 0:
            return "player_2 wins"
print (play_nims(50, 10))

