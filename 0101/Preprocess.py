# encoding: utf-8
import os
import cv2
import random
import pickle
import numpy as np
from matplotlib import pyplot as plt

class Preprocess:
    """
    Clase que extrae todas la imágenes (cambiando el alto y ancho
    de tal forma que todas tengan el mismo) de una carpeta,
    organizándolas según las categorías elegidas

    ...

    Attributes
    ----------
    training_data : list
        Información extraída de la carpeta
    labels : list
        Índices de las imágenes 
    features : list
        Imágenes

    Methods
    -------
    load_training_data()
        Recorre cada subdirectorio obteniendo la información de cada imagen

    split_and_prepare()
        Mezcla la lista con las imágenes indexadas y las separa en dos listas

    write_out()
        Se crean archivos pickle con la información de la imágenes
    """

    def __init__(self):
        """ Asigna el tamaño que tendrán las imágenes una vez procesadas
            y el nombre del directorio para extraer la imágenes, la cual
            debe contener como subdirectorios las diferentes categorías """

        self.DATADIR = "downloads"
        self.CATEGORIES = ["men","women","dog"]
        self.IMAGE_SIZE = 50;
        self.training_data = []
        self.labels = []
        self.features = []

    def load_training_data(self):
        """ Recorre cada subdirectorio obteniendo la información
            de cada imagen, cambiando su tamaño y agregando la
            nueva imagen a una lista con un índice asociado """

        for category in self.CATEGORIES:
            path = os.path.join(self.DATADIR, category)
            class_num = self.CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array,(self.IMAGE_SIZE,self.IMAGE_SIZE))
                    self.training_data.append([new_array,class_num])
                except Exception as e:
                    pass

    def split_and_prepare(self):
        """ Mezcla la lista con las imágenes indexadas y las separa
            en dos listas, normalizando el valor de cada pixel"""

        random.shuffle(self.training_data)
        for features, label in self.training_data:
            self.features.append(features)
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.IMAGE_SIZE,self.IMAGE_SIZE,1)
        self.features = self.features/255.0

    def write_out(self):
        """ Se crean dos archivos tipo pickle con la información de
            la imágenes , uno con los datos de la imagen y otro con
            el índice, simulando vectores  """

        pickle_out = open("features.pickle","wb")
        pickle.dump(self.features,pickle_out)
        pickle_out.close()

        pickle_out = open("labels.pickle","wb")
        pickle.dump(self.labels,pickle_out)
        pickle_out.close()

pr = Preprocess()
pr.load_training_data()
pr.split_and_prepare()
pr.write_out()
