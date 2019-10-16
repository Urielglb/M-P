import unittest
from identifier import Identifier
class IdentifierTest(unittest.TestCase):
    """Clase que probra los metodos de get y set de la clase identifier
        Metodos
        ------
        set()
        Revisara que el set de la clase funcione 
        
        get()
        Revisara que el get regrese correctamente el atributo de la clase
    
    """
    def set_get(self):
        """  Este metodo creará un identifier y usara su set para cambiarlo una variable cualquiera, despues verificara que su atributo no sea el del inicio """
        test = Identifier("test")   
        test.set_imgdir("cambio")
        self.assert_("test"!=test.get_imgdir())
    def get(self):
        """ Se creara un identifier con un atributo y despues se revisara que el get de ese mismo atributo"""
        test = Identifier("test")
        self.assert_("test"==test.get_imgdir())