from snap import snap

from algorithm.tpi import tpi
from utils.graph import add_nodes, add_edges
from utils.io import read_mtx


def generate_thresholds(num_of_nodes, threshold_value):
    t = {}
    for n in range(1, num_of_nodes + 1):
        t[n] = threshold_value
    return t


def main():
    num_of_nodes = 91813

    dataset = "dataset/rec-amazon.mtx"
    mtx = read_mtx(dataset)

    g = snap.TUNGraph.New()
    g = add_nodes(g, 1, num_of_nodes)
    g = add_edges(g, mtx)

    t = generate_thresholds(num_of_nodes, 1)

    result = tpi(g, t)

    print(result)
    print("SOMMA:", sum(result))


if __name__ == '__main__':
    main()
