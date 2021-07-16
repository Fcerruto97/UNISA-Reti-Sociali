from utils.console import print_dict
from utils.graph import clone
from utils.io import load_mtx_graph


def initialize_dicts(V, t, s, d, k, N):
    for v in V:
        s[v.GetId()] = 0
        d[v.GetId()] = v.GetDeg()
        k[v.GetId()] = t[v.GetId()]
        N[v.GetId()] = get_neighborhood(v)


def tpi(graph, t: dict):
    V = graph.Nodes()

    g_copy = clone(graph)

    s = dict()
    d = dict()
    k = dict()
    N = dict()

    initialize_dicts(V, t, s, d, k, N)

    iterazione = 0

    while not g_copy.Empty():

        print("iterazione", iterazione)

        flag, node_id = check_case1(g_copy, k, d)

        if flag:  # case 1
            s[node_id] = s[node_id] + k[node_id] - d[node_id]
            k[node_id] = d[node_id]

            if k[node_id] == 0:
                g_copy.DelNode(node_id)

        else:  # case 2
            argmax_dict = dict()
            for x in g_copy.Nodes():
                node_id = x.GetId()
                if d[node_id] != 0:
                    argmax_dict[node_id] = (k[node_id] * (k[node_id] + 1)) / (d[node_id] * (d[node_id] + 1))

            target_node_id = argmax_key_dict(argmax_dict)

            for u in N[target_node_id]:
                d[u] = d[u] - 1
                N[u].remove(target_node_id)

            g_copy.DelNode(target_node_id)

        iterazione += 1

    # print("s =>", s)
    # print("d => ", d)
    # print("k => ", k)
    # print("N => ", N)
    return s


def get_neighborhood(v) -> set:
    return set([e for e in v.GetOutEdges()])


def check_case1(g, k, d):
    # inizializzazione dizionario flag
    flag = {}
    for v in g.Nodes():
        flag[v.GetId()] = False

    # check sulla condizione k(v) > d(v) per ogni nodo
    for v in g.Nodes():
        if k[v.GetId()] > d[v.GetId()]:
            flag[v.GetId()] = True

    # restituzione del primo nodo per cui k(v) > d(v) è vero
    for k, _ in flag.items():
        if flag[k]:
            return True, k

    # non esiste alcun nodo per il quale k(v) > d(v) è vero
    return False, None


def argmax_key_dict(d):
    """
    Restituisce la chiave associata al nodo con il valore massimo
    :param d:
    :return:
    """
    return max(d, key=d.get)


def test_grafo_tss():
    g = load_mtx_graph("../dataset/grafo-esempio-tss.mtx", 1, 8)

    t = {}
    for i in range(1, g.GetNodes() + 1):
        t[i] = 3

    # print("soglie:", t)
    # draw(g, "test.png")

    result = tpi(g, t)
    print_dict(result)


def test_paper_tpi():
    g = load_mtx_graph("../dataset/grafo-esempio-tpi.mtx", 1, 7)

    t = {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 6,
        7: 6}

    result = tpi(g, t)
    print_dict(result)


if __name__ == '__main__':
    # test_grafo_tss()
    test_paper_tpi()
