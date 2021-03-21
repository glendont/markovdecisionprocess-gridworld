from model.MDP import MDP
from algorithms.valueiteration import get_expected_utility
import random

def policy_iteration(mdp, k):
    utilities, policies = {}, {}
    # Local dictionaries for visualisation
    U_iterations = {}

    for state in mdp.states:
        utilities[state] = 0
        policies[state] = mdp.actions[random.randint(0, 3)]  # Randomise initial policy
        U_iterations[state] = [0]

    unchanged = False
    num_iterations = 0

    while not unchanged:
        utilities, new_iteration_utilities = policy_evaluation(policies, utilities, mdp, k)
        policies, unchanged = policy_improvement(mdp, utilities, policies, unchanged)
        num_iterations += 1
        for state in mdp.states:
            U_iterations[state].extend(new_iteration_utilities[state])

    return {
        'optimal_policy': policies,
        'U_current': utilities,
        'U_iterations': U_iterations,
        'num_iterations': num_iterations,
    }

def policy_evaluation(policies, utilities, mdp, k):
    U_updated = {}
    new_iteration_utilities = {}

    for state in mdp.states:
        new_iteration_utilities[state] = []

    for i in range(int(k)):
        for state in mdp.states:
            # We use get_expected_utility to calculate ∑s′P(s′|s, a)U[s′] where we replace a with the action under π
            expected_utility = get_expected_utility(mdp, state, policies[state], utilities)

            # U_i+1(s) ← R(s) + γ ∑s′P (s'|s, π_i(s)) U_i(s')
            U_updated[state] = mdp.reward_function(state) + mdp.discount * expected_utility

        for state in mdp.states:
            utilities[state] = U_updated[state]

    for state in mdp.states:
        new_iteration_utilities[state].append(U_updated[state])

    return (utilities, new_iteration_utilities)


def policy_improvement(mdp, utilities, policies, unchanged):
    updated_policies = policies
    unchanged = True

    for state in mdp.states:
        # 1. Find max ∑ a∈A(s) P(s′ |s,a) U[s′]
        max_expected_utility = float('-inf')
        best_action = None

        for action in mdp.actions:
            expected_utility = get_expected_utility(mdp, state, action, utilities)
            if expected_utility > max_expected_utility:
                max_expected_utility = expected_utility
                best_action = action

        # 2. Find ∑ s' P(s′ |s,π[s]) U[s′]
        policy_utility = get_expected_utility(mdp, state, policies[state], utilities)

        # 3. Compare
        if max_expected_utility > policy_utility:
            updated_policies[state] = best_action
            unchanged = False

    return (updated_policies, unchanged)



