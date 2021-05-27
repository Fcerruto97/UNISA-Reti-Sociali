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
    Aggiunge gli archi a un grafo dove sono stati già aggiunti i nodi
    :param graph: snap graph
    :param mtx: scipy.sparse.coo_matrix
    :return:
    """
    for i, j, v in zip(mtx.row, mtx.col, mtx.data):
        graph.AddEdge(int(i), int(j))
    return graph
