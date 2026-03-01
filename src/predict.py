import pickle


def load_model(path):
    return pickle.load(open(path, "rb"))