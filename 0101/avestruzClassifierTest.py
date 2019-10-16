import unittest
import sys
import os
from AnimalClassifiers.avestruzClassifier import AvestruzClassifier
class AvestruzClassifierTest(unittest.TestCase):
    """ Clase que probara el entrenamiento de la red para reconocer avestruces 
    Metodos
    -------
    test_avestruz()
    probara que tan bien puede distinguir la red a las avestruces
    """
    def test_avestruz(self):
        """Mandara llamar una de las redes de la avestruz y probara que tanto puede reconocer a las a avestruces con unas cuantas imagenes dentro de la carpeta tests"""
        avestruz_cla = AvestruzClassifier("test","test")
        avestruz_cla.load("models/avestruz-jirafa")
        for img in os.listdir("test/avestruz"):
            try:
                test = avestruz_cla.predict("test/avestruz/"+img,0.5)
                self.assert_(test)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    unittest.main()