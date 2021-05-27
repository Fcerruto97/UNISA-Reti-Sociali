from snap import snap

from utils.graph import add_nodes, add_edges
from utils.io import read_mtx


def main():
    dataset = "dataset/rec-amazon.mtx"
    mtx = read_mtx(dataset)

    g = snap.TUNGraph.New()
    add_nodes(g, 1, 91813)
    add_edges(g, mtx)


if __name__ == '__main__':
    main()
