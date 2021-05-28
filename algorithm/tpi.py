from utils.graph import clone
from utils.io import load_mtx_graph


def print_dict(d):
    for k, v in d.items():
        print(k, ":", v)


def print_nodes_id(g):
    for v in g:
        print(v.GetId())


def tpi(graph, t: dict):
    V = graph.Nodes()

    g_copy = clone(graph)

    s = dict()
    d = dict()
    k = dict()
    N = dict()

    for v in V:
        s[v.GetId()] = 0
        d[v.GetId()] = v.GetDeg()
        k[v.GetId()] = t[v.GetId()]
        N[v.GetId()] = get_neighborhood(v)

    while not g_copy.Empty():

        for v in g_copy.Nodes():

            if k[v.GetId()] > d[v.GetId()]:  # case 1
                s[v.GetId()] = s[v.GetId()] + k[v.GetId()] - d[v.GetId()]
                k[v.GetId()] = d[v.GetId()]

                if k[v.GetId()] == 0:
                    g_copy.DelNode(v.GetId())

            else:  # case 2
                argmaxdict = dict()
                for x in g_copy.Nodes():
                    argmaxdict[x.GetId()] = (k[x.GetId()] * (k[x.GetId()] + 1)) / (d[x.GetId()] * (d[x.GetId()] + 1))

                target_node_id = argmax_key_dict(argmaxdict)

                for u in N[target_node_id]:
                    d[u] = d[u] - 1
                    N[u] = N[u].remove(target_node_id)

                g_copy.DelNode(target_node_id)
    return s


def get_neighborhood(v) -> set:
    return set([e for e in v.GetOutEdges()])


def test():
    g = load_mtx_graph("../dataset/test-matrixmarket-general.mtx", 1, 4)

    t = {}
    for i in range(1, g.GetNodes() + 1):
        t[i] = 1

    result = tpi(g, t)

    print_dict(result)


def argmax_key_dict(d):
    """
    Restituisce la chiave associata al nodo con il valore massimo
    :param d:
    :return:
    """
    return max(d, key=d.get)


def test_set():
    l = [1, 2, 3]
    a = set(l)
    print(a)
    a.remove(1)
    print(a)


if __name__ == '__main__':
    test()
    # test_set()
