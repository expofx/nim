from nim import Nim, Bot

def play(player0="bot", player1="human", heaps=[3,4,5]):
    """
    Play game of Nim.
    """
    
    print("Welcome to Nim!")
    nim = Nim(heaps)
    players = [player0, player1]
    print(nim.heaps)
    
    while nim.winner is None:
        if players[nim.curr_player] == "bot":
            action = Bot.get_action(nim.heaps)
            print("Bot's move: ", action)
        elif players[nim.curr_player] == "human":
            # sanitize input
            while True:
                try:
                    action = int(input("Choose a heap: ")), int(input("Amount to remove: "))
                    break
                except:
                    print("Invalid input. Try again.")
            
        nim.move(action)
        print(nim.heaps)
    
    print(f"The {players[nim.winner]} won!")

if __name__ == "__main__":
    play("bot", "human", [3,5,7,9])