from snap import snap


def create_graph():
    FILE_NAME = "ForestGraph"

    # create a graph TNGraph
    G1 = snap.TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddEdge(1, 5)
    G1.AddEdge(5, 1)
    G1.AddEdge(5, 32)
    print(G1)

    # generate a network using Forest Fire model
    G3 = snap.GenForestFire(1000, 0.35, 0.35)
    # save and load binary
    FOut = snap.TFOut(FILE_NAME + ".graph")
    G3.Save(FOut)
    FOut.Flush()
    FIn = snap.TFIn(FILE_NAME + ".graph")
    G4 = snap.TNGraph.Load(FIn)
    # save and load from a text file
    snap.SaveEdgeList(G4, FILE_NAME + ".txt", "Save as tab-separated list of edges")
    G5 = snap.LoadEdgeList(snap.TNGraph, FILE_NAME + ".txt", 0, 1)


if __name__ == '__main__':
    create_graph()
