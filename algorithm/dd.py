import random

from snap import snap

from utils.graph import add_edges_random, add_nodes, draw
from utils.io import read_mtx


def generate_edges_prob(seed, mtx):
    random.seed(seed)
    d = {}
    for i, j, _ in zip(mtx.row, mtx.col, mtx.data):
        d[str(int(i) + 1) + "," + str(int(j) + 1)] = random.random()
    return d


def dd_algorithm(mtx, num_of_nodes, edges_prob, seed):
    g = snap.TUNGraph.New()
    g = add_nodes(g, 1, num_of_nodes)
    g = add_edges_random(g, mtx, edges_prob, seed)
    return g


def main():
    dataset = "../dataset/grafo-esempio-tss.mtx"
    mtx = read_mtx(dataset)

    ht = generate_edges_prob(42, mtx)
    g = dd_algorithm(mtx, 8, ht, 42)
    draw(g, "../out/" + "dd_example" + ".png")


if __name__ == '__main__':
    main()
