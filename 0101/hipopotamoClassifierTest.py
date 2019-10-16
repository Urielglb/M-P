import unittest
import sys
import os
from AnimalClassifiers.hipopotamoClassifier import HipopotamoClassifier
class PinguinoClassifierTest(unittest.TestCase):
    """ Clase que probara el entrenamiento de la red para reconocer hipopotamos
    Metodos
    -------
    test_hipopotamos()
    probara que tan bien puede distinguir la red a los hipopotamos
    """
    def test_hipopotamo(self):
        """Mandara llamar una de las redes del hipopotamo y probara que tanto puede reconocer a los hipopotamos con unas cuantas imagenes dentro de la carpeta tests"""
        hipopotamo_cla = HipopotamoClassifier("test","test")
        hipopotamo_cla.load("models/hipopotamo-avestruz")
        for img in os.listdir("test/hipopotamo"):
            try:
                test = hipopotamo_cla.predict("test/cuyo/"+img,0.5)
                self.assert_(test)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    unittest.main()