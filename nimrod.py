import random
import math

class Nim:
    def __init__(self, num_heaps, heap_sizes, curr_player="agent", mode="nim"):
        self.num_heaps = num_heaps
        self.heaps = heap_sizes
        self.turn = 0
        self.winner = None
        self.curr_player = curr_player
        self.players = ["agent", "human"]
        self.mode = mode
        
        # assert self.mode == "nim" or self.mode == "wythoff", "Invalid mode"
        # if mode == "wythoff":
        #     assert num_heaps == 2, "Wythoff game must have 2 heaps"
        assert self.curr_player == "agent" or self.curr_player == "human", "Invalid player"

    def play(self):
        print(f"Heaps: {self.heaps}")
            
        while self.winner == None:
            
            if self.curr_player == "agent":
                self.agent_move()
            elif self.curr_player == "human":
                self.move()
                
            print(f"Heaps: {self.heaps}")
            if self.heaps == [0]*self.num_heaps:
                self.winner = self.curr_player
                print(f"{self.winner} wins!")
            
            self.curr_player = self.players[(self.players.index(self.curr_player)+1)%2]    # switch players
            self.turn += 1
        
    def move(self):
        print("Your turn")
        
        try:
            if self.mode == "nim":
                heap = int(input("Heap: "))
                while heap < 1 or heap > self.num_heaps or self.heaps[heap-1] == 0:
                    print("Invalid move")
                    heap = int(input("Heap: "))
            
                num = int(input("Amount to remove: "))
                while num < 1 or num > self.heaps[heap-1]:
                    print("Invalid move")
                    num = int(input("Amount to remove: "))
                
                self.heaps[heap-1] -= num
            
            # elif self.mode == "wythoff":
            #     heap = int(input("Heap [1,2,all]: "))
            #     while heap != 1 and heap != 2 and heap != "all":
            #         print("Invalid move")
            #         heap = int(input("Heap [1,2,all]: "))
                    
            #     num = int(input("Amount to remove: "))
            #     if heap == 1 or heap == 2:
            #         while num < 1 or num > self.heaps[heap-1]:
            #             print("Invalid move")
            #             num = int(input("Amount to remove: "))
            #         self.heaps[heap-1] -= num
            #     elif heap == "all":
            #         while num < 1 or num > min(self.heaps):
            #             print("Invalid move")
            #             num = int(input("Amount to remove: "))
            #         self.heaps[0] -= num
            #         self.heaps[1] -= num
                
            self.turn += 1
            
        except:
            print("Invalid move")
            self.move()
            
    def agent_move(self):
        print("Agent's turn")
        
        if self.mode == "nim":
            # implement Sprague-Grundy theorem
            nim_sum = 0
            for heap in self.heaps:
                nim_sum ^= heap
                
            if nim_sum == 0:    # make a random move if there is no winning strategy
                heap = random.randint(0, self.num_heaps-1)
                num = random.randint(1, self.heaps[heap])
                self.heaps[heap] -= num
            else:
                for i in range(self.num_heaps):
                    if self.heaps[i] > (self.heaps[i]^nim_sum):
                        self.heaps[i] -= (self.heaps[i] - (self.heaps[i]^nim_sum))  # make move that will result in nim_sum AKA xor of heaps = 0
                        break
        
        # elif self.mode == "wythoff":
            
            
if __name__ == "__main__":
    nim = Nim(3, [3, 4, 5]) # 3 heaps, sizes 3, 4, 5
    nim.play()
    # wythoff = Nim(2, [3, 4], mode="wythoff") # 2 heaps, sizes 3, 4
    # wythoff.play()