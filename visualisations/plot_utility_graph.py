import matplotlib.pyplot as plt

def plot_utility_graph(num_iterations,U_iterations,title):
    iteration_list=[]
    utility_list=U_iterations.get((0, 0))

    for i in range(0,len(utility_list)):
        iteration_list.append(i)

    plt.figure(figsize=(24, 12))
    plt.title(title, size=18)
    plt.grid()
    labels = []
    plt.plot(iteration_list, utility_list)
    plt.axis([min(iteration_list), max(iteration_list), min(utility_list)-5, max(utility_list)])

    for key in U_iterations.keys():
        plt.plot(iteration_list, U_iterations.get(key), label=key)
        labels.append("State" + str(key))

    plt.xlabel('Number of Iterations', fontsize=20)
    plt.ylabel('Utility Estimates', fontsize=20)
    # plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.75), ncol=3, prop={'size': 20})
    plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5),prop={'size': 15})
    plt.xticks(fontsize=25)

    title= title.replace(" ", "")
    plt.savefig('output/' + title + '.png')
    plt.show()
