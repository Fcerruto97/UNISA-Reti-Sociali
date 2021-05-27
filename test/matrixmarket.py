from snap import snap

from utils.graph import add_nodes, add_edges, draw
from utils.io import read_mtx


def matrixmarket_general():
    dataset = "../dataset/test-matrixmarket-general.mtx"
    mtx = read_mtx(dataset)

    g = snap.TUNGraph.New()
    add_nodes(g, 1, 5)
    add_edges(g, mtx)

    draw(g, "../out/test-matrixmarket-general.png")


if __name__ == '__main__':
    matrixmarket_general()
