from scipy.io import mmread


def read_mtx(path):
    return mmread(path)
