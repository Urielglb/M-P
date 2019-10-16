import sys
import unittest
from AnimalClassifiers.classifier import Classifier
class ClassifierTest(unittest.TestCase):
    """Clase que probara las funciones save y load de la clase Clasifier 
        Metodos
        -------
        test_save():
        Metodo que comprobara si el classifier se guarda correctamente

        test_load():
        Metodo que comprobrara si el classifier no lanza alguna excepcion al intentar cargar otro classifier
        
    """
    def test_save_(self):
        """ Creara una red  y la una vez guardada verificara que se creen los documentos con el nombre que se le da con la terminacion .h5 y .json"""
        classifier_save_test = Classifier("data/train","data/test","test")
        classifier_save_test.cnn_construction()
        classifier_save_test.save("test")
        try:
            json_creado = open("test.json","r")
            self.assert_(True)
        except IOError as fallo_guardar:
            self.assert_(False)
        try:
            h5_guardado = open("test.h5","r")
            self.assert_(True)
        except IOError as fallo_guardar:
            self.assert_(False)
        
    def test_load(self):
        """Se creara un classifier y se verificara que no lance ningun error al cargar los documentos creados en test_safe()"""
        classifier_load_test = Classifier("data/train","data/test","test")
        try:
            classifier_load_test.load("test")
            self.assert_(True)
        except Exception as fallo_abrir:
            self.assert_(False)

if __name__ == "__main__":
    unittest.main()