from nim import Nim, Bot
from q import Q

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
            while True:
                try:
                    action = int(input("Choose a heap: ")), int(input("Amount to remove: "))
                    break
                except:
                    print("Invalid input. Try again.")
            if action[1] < 1 or action[0] < 0 or action[0] > len(nim.heaps)-1:
                print("Invalid move. Try again.")
                continue
            elif action[1] > nim.heaps[action[0]]:
                print("Invalid move. Try again.")
                continue
        elif players[nim.curr_player] == "q":
            action = q.get_action(nim.heaps)
            print("Q-learning agent's move: ", action)
            
        nim.move(action)
        print(nim.heaps)
    
    print(f"The {players[nim.winner]} won!")

if __name__ == "__main__":
    q = Q()
    q.train(100000)
    # print(q.q)
    play("q", "human", [3,4,5])
    