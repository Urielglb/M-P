
# encoding: utf-8
from AnimalClassifiers.classifier import Classifier


class AvestruzClassifier(Classifier):
    """
    Clasificador de avestruz.
    ...

    Methods
    -------
    __init__()
        Constructor del clasificador de avestruz
    """

    def __init__(self ,data_dir, test_dir):
        """
        Constructor, recibe data_dir directorio con las imagenes de avestruz y
        otro animal para entrenar la red"""
        super(avestruzClassifier, self).__init__(data_dir, test_dir, 'avestruz')

  
if __name__ == '__main__':

    data_dir = "data/train/"
    test_dir = "data/test/"
    avestruzCla = avestruzClassifier(data_dir,test_dir)

    avestruzCla.net_training()
    avestruzCla.save("models/avestruz")
