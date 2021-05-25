from snap import snap


def draw(graph, filename):
    labels = {}
    for NI in graph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    graph.DrawGViz(snap.gvlDot, filename, " ", labels)


def main():
    # input_file = "Wiki-Vote.txt"  # 7115 nodi
    input_file = "small.txt"  # 474 nodi

    g = snap.LoadEdgeListStr(snap.TNGraph, input_file, 0, 1)
    print("Number of Nodes: %d" % g.GetNodes())

    draw(g, "output.png")


if __name__ == '__main__':
    main()
