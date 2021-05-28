from scipy.io import mmread
from snap import snap

from utils.graph import add_nodes, add_edges


def read_mtx(path):
    return mmread(path)


def load_mtx_graph(dataset, first_node, last_node):
    mtx = read_mtx(dataset)
    g = snap.TUNGraph.New()
    add_nodes(g, first_node, last_node)
    add_edges(g, mtx)
    return g
