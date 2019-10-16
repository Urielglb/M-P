
# encoding: utf-8
from AnimalClassifiers.classifier import Classifier

class HipopotamoClassifier(Classifier):
    """

    Clasificador de hipopotamo
    ...
    Methods
    -------
    __init__()
        Constructor del clasificador de hipopotamo
    """
    def __init__(self ,data_dir, test_dir):
        """Constructor, recibe data_dir directorio con las imagenes de
        hipopotamos y otro animal para entrenar la red"""
        super(hipopotamoClassifier, self).__init__(data_dir, test_dir, 'hipopotamo')


    data_dir = "data/train/"
    test_dir = "data/test/"
    hipopotamoCla = hipopotamoClassifier(data_dir,test_dir)

    hipopotamoCla.net_training()
    hipopotamoCla.save("models/hipopotamo")
