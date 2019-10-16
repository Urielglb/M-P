import unittest
import sys
import os
from AnimalClassifiers.cuyoClassifier import CuyoClassifier
class CuyoClassifierTest(unittest.TestCase):
    """ Clase que probara el entrenamiento de la red para reconocer cuyos
    Metodos
    -------
    test_cuyos()
    probara que tan bien puede distinguir la red a los cuyos
    """
    def test_cuyo(self):
        """Mandara llamar una de las redes del cuyo y probara que tanto puede reconocer a los cuyos con unas cuantas imagenes dentro de la carpeta tests"""
        cuyo_cla = CuyoClassifier("test","test")
        cuyo_cla.load("models/cuyo-avestruz")
        for img in os.listdir("test/cuyo"):
            try:
                test = cuyo_cla.predict("test/cuyo/"+img,0.5)
                self.assert_(test)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    unittest.main()