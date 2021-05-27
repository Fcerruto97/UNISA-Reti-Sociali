import pickle

from scipy.io import mmread


def save_pickle_file(data, path):
    pickle_out = open(path, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()


def load_pickle_file(path):
    pickle_in = open(path, "rb")
    return pickle.load(pickle_in)


def read_mtx(path):
    return mmread(path)
