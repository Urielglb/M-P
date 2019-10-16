# encoding: utf-8
from AnimalClassifiers.classifier import Classifier

class CuyoClassifier(Classifier):
    """
    Clasificador de cuyos.

    ...
    Methods
    -------
    __init__()
        Constructor del clasificador de cuyos
    """

    def __init__(self ,data_dir, test_dir):
        """Constructor, recibe data_dir directorio con las imagenes de cuyos y
        otro animal para entrenar la red"""
        super(CuyoClassifier, self).__init__(data_dir, test_dir, 'cuyo')

  

    data_dir = "data/train/"
    test_dir = "data/test/"
    cuyoCla = CuyoClassifier(data_dir,test_dir)

    cuyoCla.net_training()
    cuyoCla.save("models/cuyo")

