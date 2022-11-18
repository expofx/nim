from nim import Nim
import random
from copy import copy

class Q:
    """
    Q-learning agent for Nim.
    """
    
    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q = {}
        
    def get_action(self, heaps):
        """
        Get action using epsilon-greedy policy.
        """
        if random.random() < self.epsilon:  # explore
            return random.choice(self.get_actions(heaps))
        else:   # exploit
            return self.get_best_action(heaps)
        
    def get_actions(self, heaps):
        """
        Build list of all possible actions.
        """
        actions = []
        for i in range(len(heaps)):
            for j in range(1, heaps[i]+1):
                actions.append((i, j))
        return actions
    
    def get_best_action(self, heaps):
        """
        Get best action based on current Q (expected) values. If multiple actions have the same value, choose randomly.
        """
        
        best_actions = []
        max_value = float("-inf")
        
        for action in self.get_actions(heaps):
            value = self.get_value(heaps, action)
            if value > max_value:
                best_actions = [action]
                max_value = value
            elif value == max_value:
                best_actions.append(action)
                
        return random.choice(best_actions)
    
    def get_value(self, heaps, action):
        """
        Get Q value for a given state-action pair.
        """
        if (tuple(heaps), action) not in self.q:
            return 0
        return self.q[(tuple(heaps), action)]
    
    def update(self, heaps, action, reward, next_heaps):
        """
        Update Q value for a given state-action pair.
        """
        if (tuple(heaps), action) not in self.q:
            self.q[(tuple(heaps), action)] = 0
        self.q[(tuple(heaps), action)] += self.alpha * (reward + self.gamma * self.get_value(next_heaps, self.get_best_action(next_heaps)) - self.q[(tuple(heaps), action)])
        
    def train(self, num_games=1000):
        """
        Training through self play.
        """
        for _ in range(num_games):
            nim = Nim([3,4,5])
            # nim = Nim([random.randint(1, 10) for _ in range(random.randint(2, 4))]) # play with up to 4 heaps of random size
            
            # keep track of states and actions taken by each player
            states = [[], []]
            actions = [[], []]
            
            while nim.winner is None:
                action = self.get_action(nim.heaps)
                states[nim.curr_player].append(copy(nim.heaps))
                actions[nim.curr_player].append(copy(action))
                nim.move(action)
                
            # update Q values for each player
            for player in [0, 1]:
                reward = 1 if nim.winner == player else -1
                for i in range(len(states[player])):
                    self.update(states[player][i], actions[player][i], reward, states[player][i])
                
            if _ % (num_games // 10) == 0:
                print("Game", _)
                
        print("Training complete.")