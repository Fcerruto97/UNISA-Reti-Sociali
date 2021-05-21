import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def main():
    edges = pd.read_csv("ia-primary-school-proximity.edges")

    g = nx.from_pandas_edgelist(edges, "node1", "node2")

    nx.draw(g)
    plt.show()


if __name__ == '__main__':
    main()
