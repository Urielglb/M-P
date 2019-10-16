from graph import graph

class Identifier:
    """
    Clase que dada una imagen de entrada especifica que animal es en caso de
    coincidir con alguno de los 5 seleccionados

    (Jirafa, Hipopotamo, Avestruz, Cuyo y Pinguino)
    ...
    Attributes
    ----------
    __img_dir : srt
        Ruta de la imagen a identificar
    Methods
    -------
    get_imgdir()
        Devuelve la ruta de la imagen

    set_imgdir()
        Permite modificar la ruta de la imagen

    predict()
        Muestra en pantalla que animal corresponde a la imagen
    """

    def __init__(self,img_dir):
        """Le indica a la clase la ruta de la imagen a clasificar"""
        self.__img_dir = img_dir
        self.graph = graph("")
        
    def get_imgdir(self):
        """
        Returns
        -------
        srt
            Directorio que contiene imagenes del animal a clasificar"""


    def set_imgdir(self,img):
        self.__img_dir = img;

    def set_imgdir(self,img):

        """Permite cambiar el directorio de imagenes del animal
         Parameters
         ----------
         data_dir : srt
            Direccion del nuevo directorio"""


        self.__img_dir = img;

    def predict(self):
      """ Predice el animal que aparece en la imagen siguiendo la secuencia
            de una grafica completa de 5 vertices, donde cada vertice es un
            animal, y cada arista es una relacion de si o no segun el resultado
            de la CNN """
  
       if(not self.__img_dir):
           return
       print(self.get_imgdir())
       self.graph.set_image(self.get_imgdir())
       print(self.graph.quienEsEsePokemon())
       self.graph.reset()
        

if __name__ == '__main__':
    another = True
    identifier = Identifier("")
    while(another):
        print("Ruta de la imagen a predecir:")
        img = input()
        identifier.set_imgdir(img)
        identifier.predict()
        print("¿Otra vez? [S]:Si,[N]:No")
        another = (input() >= "S")

