import random

class Nim:
    """
    Create game of Nim. Takes actions from players as input and returns the winner.
    """
    def __init__(self, heaps):
        self.heaps = heaps
        self.winner = None
        self.curr_player = 0 # players are 0 and 1
        
    def move(self, action): # action is a tuple (heap, num)
        heap, num = action
        self.heaps[heap] -= num
        
        if self.heaps[heap] < 0:
            raise Exception("Invalid move")
        
        if self.heaps == [0]*len(self.heaps):
            self.winner = self.curr_player
        else:
            self.curr_player = 1 - self.curr_player
        
class Bot:
    """
    Bot that plays optimally using Sprague-Grundy theorem.
    """
    @staticmethod 
    def get_action(heaps):
        nim_sum = 0
        for heap in heaps:
            nim_sum ^= heap
            
        if nim_sum == 0:    # random move if there is no winning strategy
            heap = random.randint(0, len(heaps)-1)
            action = (heap, random.randint(1, heaps[heap]))
            return action
        else:
            for i in range(len(heaps)):
                if heaps[i] > (heaps[i]^nim_sum):   # make move that will result in nim_sum of 0
                    action = (i, heaps[i] - (heaps[i]^nim_sum)) # nim_sum^heap[i] is effectively taking heap[i] out of XOR; want to equalize heap[i] and XOR of rest of elements
                    return action