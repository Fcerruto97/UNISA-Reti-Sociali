import random
import time

from snap import snap


def draw(graph, filename):
    labels = {}
    for NI in graph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    graph.DrawGViz(snap.gvlDot, filename, " ", labels)


def add_nodes(graph, start, stop):
    """
    Aggiunge un range di nodi
    :param graph:
    :param start: primo nodo
    :param stop: ultimo nodo (incluso)
    :return: grafo con i nuovi nodi
    """
    for i in range(start, stop + 1):
        graph.AddNode(int(i))
    return graph


def add_edges(graph, mtx):
    """
    Aggiunge gli archi a un grafo dove sono stati già aggiunti i nodi.
    :param graph: snap graph
    :param mtx: scipy.sparse.coo_matrix con primo nodo uguale a zero
    :return: grafo a cui sono stati aggiunti gli archi. La numerazione parte da 1
    """
    for i, j, v in zip(mtx.row, mtx.col, mtx.data):
        graph.AddEdge(int(i) + 1, int(j) + 1)
    return graph


def add_edges_random(graph, mtx, edges_prob):
    """
    Aggiunge gli archi a un grafo dove sono stati già aggiunti i nodi.
    :param graph: snap graph
    :param mtx: scipy.sparse.coo_matrix con primo nodo uguale a zero
    :return: grafo a cui sono stati aggiunti gli archi. La numerazione parte da 1
    """
    random.seed(time.time())
    for i, j, v in zip(mtx.row, mtx.col, mtx.data):
        magicNumber = random.random()
        if magicNumber > edges_prob[str(int(i) + 1) + "," + str(int(j) + 1)]:
            graph.AddEdge(int(i) + 1, int(j) + 1)
    return graph


def clone(graph):
    return snap.ConvertGraph(type(graph), graph)
