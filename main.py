from model.constants import *
from model.Maze import Maze
from model.bonus_functions import generate_maze
from model.bonus_functions import vary_mazesize
from model.bonus_functions import vary_complexity

from algorithms.policyiteration import *
from algorithms.valueiteration import *

from visualisations.plot_utility_graph import plot_utility_graph
from visualisations.print_utilities import print_utilities
from visualisations.grid_visualisation import grid_visualisation

import time
import numpy
import threading

def wait_message():
  threading.Timer(10, wait_message).start()
  print("Please hold, the analysis is ongoing...")

if __name__ == '__main__':
    print("*********************************************************************************************************")
    print("Hello there, welcome to GridWorld! We will use this to illustrate the Markov Decision Process.")
    print("*********************************************************************************************************")

    print("Maze Creation")
    maze_input=input("1. 6x6 Maze \n2. More Complicated Maze \n")
    if (maze_input=="1"):
        print("Initialising 6x6 Maze Environment...")
        maze = Maze(GRID, REWARD_MAP, DISCOUNT)
        print("6x6 Maze Environment Created! ")
        print("Please choose your optimal policy algorithm")

        algorithm_input = input("1. Value Iteration Algorithm \n2. Policy Iteration Algorithm \n")
        if (algorithm_input=="1"):
            print("Running Value Iteration Algorithm...")

            algorithm_output = value_iteration(maze)
            final_state_utilities = algorithm_output['U_current']
            optimal_policy = algorithm_output['optimal_policy']
            U_iterations = algorithm_output['U_iterations']
            num_iterations = algorithm_output['num_iterations']

            print("Optimal Policy found!")
            print("Choose the following options:")

            option_input = input("1. Grid Visualisations \n2. Utilities of all states \n3. Visualise Plot of Utility Estimates as a function of the number of iterations\n")
            if (option_input=="1"):
                grid_visualisation(optimal_policy, maze.grid, "policy")
                grid_visualisation(final_state_utilities,maze.grid,"utilities")
            elif(option_input=="2"):
                print_utilities(final_state_utilities, num_iterations, algorithm="valueiteration")
            elif(option_input=="3"):
                plot_utility_graph(num_iterations, U_iterations, title="Value Iteration")
        elif(algorithm_input=="2"):
            print("Running Policy Iteration Algorithm...")
            policy_iteration_res = policy_iteration(maze, K)

            print("Optimal Policy found!")
            algorithm_output = value_iteration(maze)

            final_state_utilities = algorithm_output['U_current']
            optimal_policy = algorithm_output['optimal_policy']
            U_iterations = algorithm_output['U_iterations']
            num_iterations = algorithm_output['num_iterations']

            print("Choose the following options:")
            option_input = input("1. Grid Visualisations \n2. Utilities of all states \n3. Visualise Plot of Utility Estimates as a function of the number of iterations\n")
            if (option_input=="1"):
                grid_visualisation(optimal_policy, maze.grid, "policy")
                grid_visualisation(final_state_utilities,maze.grid,"utilities")
            elif(option_input=="2"):
                print_utilities(final_state_utilities, num_iterations, algorithm="policyiteration")
            elif(option_input=="3"):
                plot_utility_graph(num_iterations, U_iterations, title="Policy Iteration")

    elif (maze_input=="2"):
        print("Initialising a more complicated maze environment...")
        print("Select the following optimal policy algorithms")
        algorithm_input = input("1. Value Iteration Algorithm \n2. Policy Iteration Algorithm \n")
        if(algorithm_input=="1"):
            wait_message()
            vary_mazesize(algorithm="valueiteration")
            vary_complexity(algorithm="valueiteration")
            print("Analysis complete!")
        elif(algorithm_input=="2"):
            wait_message()
            vary_complexity(algorithm="policyiteration")
            vary_mazesize(algorithm="policyiteration")
            print("Analysis complete!")


