from snap import snap

from utils.graph import add_nodes, add_edges
from utils.io import read_mtx


def main():
    input_file = "rec-amazon.mtx"
    mtx = read_mtx(input_file)

    g = snap.TUNGraph.New()
    add_nodes(g, 0, 91813)
    add_edges(g, mtx)


if __name__ == '__main__':
    main()
