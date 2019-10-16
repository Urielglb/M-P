import unittest
import sys
import os
from AnimalClassifiers.pinguinoClassifier import PinguinoClassifier
class PinguinoClassifierTest(unittest.TestCase):
    """ Clase que probara el entrenamiento de la red para reconocer pinguinos
    Metodos
    -------
    test_pinguino()
    probara que tan bien puede distinguir la red a los pinguinos
    """
    def test_pinguino(self):
        """Mandara llamar una de las redes del pinguino y probara que tanto puede reconocer a los pinguinos con unas cuantas imagenes dentro de la carpeta tests"""
        pinguino_cla = PinguinoClassifier("test","test")
        pinguino_cla.load("models/cuyo-avestruz")
        for img in os.listdir("test/cuyo"):
            try:
                test = pinguino_cla.predict("test/cuyo/"+img,0.5)
                self.assert_(test)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    unittest.main()