import unittest
import sys
import os
from AnimalClassifiers.jirafaClassifier import JirafaClassifier
class JirafaClassifierTest(unittest.TestCase):
    """ Clase que probara el entrenamiento de la red para reconocer jirafas
    Metodos
    -------
    test_jirafas()
    probara que tan bien puede distingu la red a las jirafas
    """
    def test_jirafa(self):
        """Mandara llamar una de las redes de la jirafa y probara que tanto puede reconocer a las jirafas con unas cuantas imagenes dentro de la carpeta tests"""
        jirafa_cla = JirafaClassifier("test","test")
        jirafa_cla.load("models/jirafa-pinguino")
        for img in os.listdir("test/jirafa"):
            try:
                test = jirafa_cla.predict("test/jirafa/"+img,0.5)
                self.assert_(test)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    unittest.main()