
# encoding: utf-8
from AnimalClassifiers.classifier import Classifier

class JirafaClassifier(Classifier):
    """
    Clasificador de jirafa.

    ...

    -------
    __init__()
        Constructor del clasificador de jirafa
    """

    def __init__(self ,data_dir, test_dir):
        """Constructor, recibe data_dir directorio con las imagenes de jirafas y
        otro animal para entrenar la red"""
        super(JirafaClassifier, self).__init__(data_dir, test_dir, 'jirafa')

if __name__ == '__main__':

    data_dir = "data/train/"
    test_dir = "data/test/"
    jirafaCla = JirafaClassifier(data_dir,test_dir)

    jirafaCla.net_training()
    jirafaCla.save("models/jirafa")
