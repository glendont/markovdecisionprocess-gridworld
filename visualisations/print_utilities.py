from model.constants import *

def print_utilities(U_iterations, num_iterations, algorithm):
    if (algorithm == "valueiteration"):
        print("***********************************")
        print("Value Iteration Algorithm")
        print("Values of Parameters")
        print("***********************************")
        print("Discount Factor", "\t\t", ":", DISCOUNT)
        print("Utility Upper Bound", "\t",":", 100)
        print("Max Reward(Rmax)", "\t\t", ":", R_MAX)
        print("Constant 'c'", "\t\t\t", ":", C)
        print("Epilson Value", "\t\t\t", ":",EPSILON)
        print("Convergence Threshold", "\t", ":",CONVERGENCE_THRESHOLD)
        print("Number of Iterations","\t",":", num_iterations)

    elif (algorithm =="policyiteration"):
        print("***********************************")
        print("Policy Iteration Algorithm")
        print("Values of Parameters")
        print("***********************************")
        print("Discount Factor", "\t\t", ":",DISCOUNT)
        print("K","\t\t\t\t\t\t",":", K)
        print("Number of Iterations","\t",":", num_iterations)


    print("***********************************")
    print("Utility Values of all States")
    print("***********************************")
    print(" State : Value")
    for key in U_iterations.keys():
        print(key,":",U_iterations.get(key))
    print("***********************************")