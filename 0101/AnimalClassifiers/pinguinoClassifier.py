
# encoding: utf-8
from AnimalClassifiers.classifier import Classifier


class PinguinoClassifier(Classifier):
    """

    Clasificador de pinguino.
    ...
    Methods
    -------
    __init__()
        Constructor del clasificador de pinguino

    def __init__(self ,data_dir, test_dir):
        """Constructor, recibe data_dir directorio con las imágenes de pingüinos
         y otro animal para entrenar la red"""
        super(PinguinoClassifier, self).__init__(data_dir, test_dir, 'Pinguino')

    # if __name__ == '__main__':


    data_dir = "data/train/"
    test_dir = "data/test/"
    pinguinoCla = PinguinoClassifier(data_dir,test_dir)

    pinguinoCla.net_training()
    pinguinoCla.save("../models/pinguino")
    # cuyoCls.load('modeloCuyo')
    #Un ejemplo de prueba
    #cuyoCls.predict(os.path.join(dirname, testSetPath, 'Cuyo/64.shut.jpg',))
