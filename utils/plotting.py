import matplotlib.pyplot as plt


def generate_graph(threshold, cost):
    plt.plot(threshold, cost, marker=".")
    plt.xlabel('Threshold')
    plt.ylabel('Cost')
    plt.show()


if __name__ == '__main__':
    threshold = [1, 2, 3]
    cost = [150, 238, 280]

    generate_graph(threshold, cost)
