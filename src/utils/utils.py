from sklearn.datasets import load_iris



class Fonctional():
    def __init__(self) -> None:
        pass

    def get(self):
        """ return iris data"""
        data = load_iris()
        return data.data ,  data.target