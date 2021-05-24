from snap import snap


def draw(Graph):
    labels = {}
    for NI in Graph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    Graph.DrawGViz(snap.gvlDot, "output.png", " ", labels)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 10, 50)
    labels = {}
    for NI in UGraph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    UGraph.DrawGViz(snap.gvlDot, "output.png", " ", labels)

    Network = snap.GenRndGnm(snap.TNEANet, 10, 50)
    labels = {}
    for NI in Network.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    Network.DrawGViz(snap.gvlDot, "output.png", " ", labels)


def main():
    G = snap.LoadEdgeListStr(snap.TNGraph, "Wiki-Vote.txt", 0, 1)
    print("Number of Nodes: %d" % G.GetNodes())


if __name__ == '__main__':
    main()
