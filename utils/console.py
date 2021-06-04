def print_dict(d):
    for k, v in d.items():
        print(k, ":", v)


def print_nodes_id(g):
    for v in g:
        print(v.GetId())
