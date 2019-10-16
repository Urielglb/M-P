# encoding: utf-8
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from PIL import Image
import numpy as np

class Classifier:
    """
    Clase que modela que entrena un modelo para clasificar a un animal
    ...
    Attributes
    ----------
    data_dir : srt
        Directorio que contiene imagenes del animal a clasificar
    test_dir : srt
        Directorio que contiene imagenes del animal para probar
    name : srt
        Nombre del animal a clasificar
    classifier
        CNN
    image_transformations : dic
        Contiene las imagenes con modificaciones para el entrenamiento
    Methods
    -------
    cnn_construction()
        Se agregan las primeras capas a la red
    net_connection()
        Se agregan capas densas a la red
    image_transformation()
        Normaliza el formato y dimension de las imagenes
    net_training()
        Entrenamiento de la CNN
    save()
        Guarda el entrenamiento de la CNN
    load()
        Carga el entrenamiento de la CNN
    predict()
        Cambia el umbral
    """

    def __init__(self,data_dir,test_dir,name):
        """Le indica a la clase que animal se clasificara
           y en donde se encuentra dicha informacion"""

        self.data_dir = data_dir
        self.test_dir = test_dir
        self.name = name
        self.classifier = Sequential()
        self.image_transformations = []

    def get_data_dir(self):
        """
        Returns
        -------
        srt
            Directorio que contiene imagenes del animal a clasificar"""

        return data_dir

    def set_data_dir(self,data_dir):
        """Permite cambiar el directorio de imagenes del animal
         Parameters
         ----------
         data_dir : srt
            Direccion del nuevo directorio"""

        self.data_dir = data_dir

    def get_test_dir(self):
        """
        Returns
        -------
        srt
            Directorio que contiene imagenes del animal para probar"""

        return test_dir

    def set_test_dir(self,test_dir):
        """Permite cambiar el directorio de imagenes a probar
         Parameters
         ----------
         test_dir : srt
             Direccion del nuevo directorio"""

        self.test_dir = test_dir

    def get_name(self):
        """
        Returns
        -------
        srt
            Nombre del animal a clasificar"""

        return name

    def set_name(self,name):
        """Permite asignar un nuevo nombre de animal a clasificar
         Parameters
         ----------
         name : srt
             Nombre del animal"""

        self.name = name

    def cnn_construction(self):
        """ Se agrega las primeras capas a las red
            De convolucion, activacion y reduccion """
        #Convolution2D(tamaño del arreglo, input_shape = (dimensiones de la imagen y a color), función de activación)
        self.classifier.add(Convolution2D(32,3,3, input_shape = (64,64,3), activation = "relu"))
        self.classifier.add(MaxPooling2D(pool_size=(2,2)))
        self.classifier.add(Flatten())

    def net_connection(self):
        """ Se agregan capas densas conectadas por capas de activacion,
            aqui se define que la red sera binaria, es decir, es detectara si la
            imagen es del animal deseado o es otro, y nos mostrara el progreso"""

        self.classifier.add(Dense(output_dim = 128, activation = "relu"))
        self.classifier.add(Dense(output_dim = 1, activation = "sigmoid"))
        self.classifier.compile(optimizer = "adam", loss = "binary_crossentropy",metrics = ["accuracy"])

    def image_transformation(self):
        """ Normaliza el formato y dimension de las imagenes generando mas
            informacion para probar la red"""

        train_datagen = ImageDataGenerator(
            rescale = 1./255,
            shear_range = 0.2,
            zoom_range = 0.2,
            horizontal_flip = True)
        test_datagen = ImageDataGenerator(
            rescale = 1./255)
        training_set = train_datagen.flow_from_directory(
            #Se indica el origen de las imágenes y el formato
            self.data_dir,
            target_size = (64,64),
            batch_size = 32,
            class_mode = "binary")
        test_set = train_datagen.flow_from_directory(
            self.test_dir,
            target_size = (64,64),
            batch_size = 32,
            class_mode = "binary")
        return train_datagen,test_datagen,training_set,test_set

    def net_training(self):
        """ Se define cuantas veces la red operará las imagenes y
            los procesos que hara para entrenar la red """

        self.cnn_construction()
        self.net_connection()
        self.image_transformations = self.image_transformation()
        self.classifier.fit_generator(
            self.image_transformations[2],
            steps_per_epoch = 50, #8000
            epochs = 30,             #10
            validation_data = self.image_transformations[3],
            validation_steps = 50) #800

    def save(self, name):
        """Guarda el entrenamiento de la CNN y los valores de precision
         Parameters
         ----------
         name : srt
             Nombre del archivo del entrenamiento """

        model_json = self.classifier.to_json()
        with open(name+".json", "w") as json_file:
            json_file.write(model_json)
        self.classifier.save_weights(name+".h5")

    def load(self, name):
        """Carga el entrenamiento de la CNN y los valores de precision
         Parameters
         ----------
         name : srt
             Nombre del archivo del entrenamiento """

        json_file = open(name+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.classifier = model_from_json(loaded_model_json)
        # load weights into new model
        self.classifier.load_weights(name+".h5")

    def predict(self, img_dir, umbral):
        """Define el umbral necesario para que la imagen dada sea
           o no el animal propuesto
         Parameters
         ----------
         img_dir : srt
             Direccion de la imagen a procesar
        Returns
        -------
        bool
            Indica si la imagen corresponde al animal propuesto"""

        test_img = image.load_img(img_dir, target_size = (64, 64))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis = 0)
        result = self.classifier.predict(test_img)
        print(result)
        return result[0][0] >= umbral