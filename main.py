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

if __name__ == '__main__':
    ######################################################################
    # 1. Value Iteration Algorithm
    ######################################################################
    # Initialise a maze environment
    maze1 = Maze(GRID, REWARD_MAP, DISCOUNT)

    # Run Value Iteration Algorithm
    value_iteration_res = value_iteration(maze1)

    # Extract outputs from Value Iteration Algorithm
    final_state_utilities = value_iteration_res['U_current']
    optimal_policy = value_iteration_res['optimal_policy']
    U_iterations = value_iteration_res['U_iterations']
    num_iterations = value_iteration_res['num_iterations']

    # Visualise Outputs
    # grid_visualisation(optimal_policy, maze1.grid, "policy")
    # grid_visualisation(final_state_utilities,maze1.grid,"utilities")
    print_utilities(final_state_utilities, num_iterations, algorithm="valueiteration")
    # plot_utility_graph(num_iterations, U_iterations, title="Value Iteration")

    ######################################################################
    # 2. Policy Iteration Algorithm
    ######################################################################
    # # Initialise a maze environment
    # maze2 = Maze(GRID, REWARD_MAP, DISCOUNT)
    #
    # # Run Policy Iteration Algorithm
    # policy_iteration_res = policy_iteration(maze2, K)
    #
    # # Extract outputs from Policy Iteration Algorithm
    # policies = policy_iteration_res['optimal_policy']
    # utilities = policy_iteration_res['U_current']
    # U_iterations = policy_iteration_res['U_iterations']
    # num_iterations=policy_iteration_res['num_iterations']
    #
    # # Visualise Outputs
    # print_utilities(utilities, num_iterations, algorithm="policyiteration")
    # grid_visualisation(policies, maze2.grid, "policy")
    # grid_visualisation(utilities,maze2.grid,"utilities")
    # plot_utility_graph(num_iterations, U_iterations, title="Policy Iteration")

    ######################################################################
    # # 3a. Bonus Question - Generating a more Complicated Map
    ######################################################################
    # # Initialise a more complicated maze environment with 13x13 states
    # bigger_grid = generate_maze(6)
    # maze3a = Maze(bigger_grid, REWARD_MAP, DISCOUNT)
    # start=time.time()
    #
    # # Run Value Iteration Algorithm
    # value_iteration_res = value_iteration(maze3a)
    #
    # # Extract outputs from Value Iteration Algorithm
    # final_state_utilities = value_iteration_res['U_current']
    # optimal_policy = value_iteration_res['optimal_policy']
    # U_iterations = value_iteration_res['U_iterations']
    # num_iterations = value_iteration_res['num_iterations']
    #
    # # Visualise Outputs
    # grid_visualisation(optimal_policy, maze3a.grid, "policy")
    # grid_visualisation(final_state_utilities,maze3a.grid,"utilities")
    # print_utilities(final_state_utilities, num_iterations, algorithm="valueiteration")
    # plot_utility_graph(num_iterations, U_iterations, title="Value Iteration")
    #
    # # Varying maze size and maze complexity to analyse performance of value and policy iterations
    # vary_mazesize(algorithm="valueiteration")
    # vary_complexity(algorithm="valueiteration")


