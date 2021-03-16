# coding=utf-8
# IMPLEMENT MAZE CLASS WHICH INHERITS FROM MDP

from MDP import MDP

class Maze(MDP):
    """
    Maze is a 2D square array where each square can take different values.

    Possible squares:
        - ' ': white
        - 'G': green
        - 'B': brown
        - 'W': wall

    """
    def __init__(self, grid, reward_map, discount):
        """
        Initialises:x
            - grid which will hold the states and possible actions in the maze. 
            = reward map of each state 
            = mdp
                - states
                = actions
                - discount

        """
        self.grid = grid
        self.reward_map = reward_map

        states = {}
        for x in range(len(grid)):
            for y in range(len(grid)):
                # ONLY NEED TO HOLD NON-WALL STATES
                if grid[x][y] != 'W':
                    states[(x,y)] = {}

        actions = ['^', 'v', '<', '>']

        super().__init__(states, actions, discount)

        #initialise the actions and probabilities for each state
        for state in states:
            next_actions = {}
            for action in actions:
                next_actions[action] = self.get_next_states(state, action)
            states[state] = next_actions

    def transition_model(self, state, action, next_state) -> float:
        """
        returns transition model: P (s′ | s, a)
        """
        return self.get_next_states(state, action)[next_state]['probability']

    def reward_function(self, state):
        """
        returns reward of given state: R(s)
        """
        square = self.grid[state[0]][state[1]]
        reward = self.reward_map[square]

        return reward

    def get_next_states(self, state, action):
        """
        Given current state and action to take, return all possible next states

        """
        if action == '^':
            up_state =(state[0] - 1, state[1])
            left_state = (state[0], state[1]-1)
            right_state = (state[0], state[1]+1)
            
            #CHECK If STATES ARE VALID
            if up_state in self.states:
                actual_up_state = up_state 
            else:
                actual_up_state = state  
            
            if left_state in self.states:
                actual_left_state = left_state 
            else:
                actual_left_state = state 

            if right_state in self.states:
                actual_right_state = right_state 
            else:
                actual_right_state = state 

            next_states = { 
                actual_up_state: {
                    'probability': 0.8,
                }, 
                actual_left_state: {
                    'probability': 0.1,
                }, 
                actual_right_state: {
                    'probability': 0.1,
                }, 
            }

        elif action  == 'v':
            down_state =  (state[0]+1, state[1])
            left_state = (state[0], state[1]-1)
            right_state = (state[0], state[1]+1)

            #CHECK If STATES ARE VALID
            if down_state in self.states:
                actual_down_state = down_state 
            else:
                actual_down_state = state  

            if left_state in self.states:
                actual_left_state = left_state 
            else:
                actual_left_state = state 

            
            if right_state in self.states:
                actual_right_state = right_state 
            else:
                actual_right_state = state  

            next_states = {
                actual_down_state: {
                    'probability': 0.8,
                }, 
                actual_left_state: {
                    'probability': 0.1,
                }, 
                actual_right_state: {
                    'probability': 0.1,
                },
            }

        elif action  == '<':
            left_state = (state[0], state[1]-1)
            down_state =  (state[0]+1, state[1])
            up_state =(state[0] - 1, state[1])

            #CHECK If STATES ARE VALID
            if left_state in self.states:
                actual_left_state = left_state 
            else:
                actual_left_state = state  

            if down_state in self.states:
                actual_down_state = down_state 
            else:
                actual_down_state = state  

            if up_state in self.states:
                actual_up_state = up_state 
            else:
                actual_up_state = state 

            next_states = {
                actual_left_state: {
                    'probability': 0.8,
                },
                actual_up_state: {
                    'probability': 0.1,
                }, 
                actual_down_state: {
                    'probability': 0.1,
                }, 
            }

        else:  # action  == '>'
            right_state = (state[0], state[1]+1)
            up_state =(state[0] - 1, state[1])
            down_state = (state[0]+1, state[1])

            #CHECK If STATES ARE VALID
            if right_state in self.states:
                actual_right_state = right_state 
            else:
                actual_right_state = state  

            if up_state in self.states:
                actual_up_state = up_state 
            else:
                actual_up_state = state  

            if down_state in self.states:
                actual_down_state = down_state 
            else:
                actual_down_state = state  

            next_states = {
                actual_right_state: {
                    'probability': 0.8,
                },
                actual_up_state: {
                    'probability': 0.1,
                }, 
                actual_down_state: {
                    'probability': 0.1,
                },
            }

        return next_states



