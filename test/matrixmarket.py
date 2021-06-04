from snap import snap

from utils.graph import add_nodes, add_edges, draw
from utils.io import read_mtx


def matrixmarket_general():
    dataset_name = "grafo-esempio-tss"
    mtx = read_mtx("../dataset/" + dataset_name + ".mtx")

    g = snap.TUNGraph.New()
    add_nodes(g, 1, 8)
    add_edges(g, mtx)

    draw(g, "../out/" + dataset_name + ".png")


if __name__ == '__main__':
    matrixmarket_general()
