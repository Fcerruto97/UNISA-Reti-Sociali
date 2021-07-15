import time

from snap import snap

from algorithm.dd import generate_edges_prob, dd_algorithm
from algorithm.tpi import tpi
from utils.graph import add_nodes, add_edges
from utils.io import read_mtx


def generate_thresholds(num_of_nodes, threshold_value):
    t = {}
    for n in range(1, num_of_nodes + 1):
        t[n] = threshold_value
    return t


def generate_degree_threshold(g, i):
    t = {}
    for v in g.Nodes():
        t[v.GetId()] = round(v.GetDeg() / i)
    return t


def exp_static_threshold(dataset, num_of_nodes, threshold):
    mtx = read_mtx(dataset)

    g = snap.TUNGraph.New()
    g = add_nodes(g, 1, num_of_nodes)
    g = add_edges(g, mtx)

    t = generate_thresholds(g, threshold)

    result = tpi(g, t)

    print(result)
    print("SOMMA:", sum(result))


def exp_degree_proportional_threshold(dataset, num_of_nodes, i):
    mtx = read_mtx(dataset)

    g = snap.TUNGraph.New()
    g = add_nodes(g, 1, num_of_nodes)
    g = add_edges(g, mtx)

    t = generate_degree_threshold(g, i)

    result = tpi(g, t)

    print(result)
    print("> COSTO TOT:", sum(result))


def exp_dd_static_threshold(dataset, num_of_nodes, threshold):
    mtx = read_mtx(dataset)

    edges_prob = generate_edges_prob(42, mtx)

    results = {}
    for i in range(10):
        g = dd_algorithm(mtx, num_of_nodes, edges_prob, time.time())

        t = generate_thresholds(g, threshold)

        result = tpi(g, t)
        results[i] = sum(result.values())

    print(results)
    print("Risultato medio:", sum(results.values()) / len(results.values()))


def exp_dd_degree_proportional_threshold(dataset, num_of_nodes, threshold):
    mtx = read_mtx(dataset)

    edges_prob = generate_edges_prob(42, mtx)

    results = {}
    for i in range(2, 12):
        g = dd_algorithm(mtx, num_of_nodes, edges_prob, time.time())

        t = generate_degree_threshold(g, threshold)

        result = tpi(g, t)
        results[i] = sum(result.values())

    print(results)
    print("Risultato medio:", sum(results.values()) / len(results.values()))


def main():
    num_of_nodes = 2970
    dataset = "dataset/socfb-Wellesley22.mtx"

    # exp_degree_proportional_threshold(dataset, num_of_nodes, 2)
    # exp_dd_static_threshold(dataset, num_of_nodes, 1)
    # exp_dd_static_threshold(dataset, num_of_nodes, 1)
    exp_dd_degree_proportional_threshold(dataset, num_of_nodes, 1)


if __name__ == '__main__':
    main()
