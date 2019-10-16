from AnimalClassifiers.classifier import Classifier

class graph:

    def __init__(self,image):
        self.image = image
        self.nodos_usados = ["C","H","J"]
    
    def set_image(self,image):
        self.image = image

    def get_image(self):
        return image
    
    def load(self,m):
        path_to = "models/"
        c = Classifier("random", "random", "random")
        c.load(path_to+m)
        return c
    def reset(self):
        self.nodos_usados = ["C","H","J"]

    def j_p(self, thresh):
        c = self.load("jirafa-pinguino")
        return c.predict(self.image, thresh)

    def j_a(self, thresh):
        c = self.load("jirafa-avestruz")
        return c.predict(self.image, thresh)

    def j_h(self, thresh):
        c = self.load("jirafa-hipopotamo")
        return c.predict(self.image, thresh)

    def c_j(self, thresh):
        c = self.load("cuyo-jirafa2")
        return c.predict(self.image, thresh)

    def p_a(self, thresh):#falta
       # c = self.load("pinguino-avestruz")
        return True;
        return c.predict(self.image, thresh)

    def p_h(self, thresh):
        c = self.load("pinguino-hipopotamo2")
        return c.predict(self.image, thresh)

    def c_p(self, thresh):
        c = self.load("cuyo-pinguino2")
        return c.predict(self.image, thresh)

    def a_h(self, thresh):
        c = self.load("avestruz-hipopotamo2")
        return c.predict(self.image, thresh)

    def a_c(self, thresh):
        c = self.load("avestruz-cuyo")
        return c.predict(self.image, thresh)

    def h_c(self, thresh):
        c = self.load("hipopotamo-cuyo")
        return c.predict(self.image, thresh)

    def j_c(self, thresh):
        return not self.c_j(thresh)

    def p_c(self, thresh):
        return not self.c_p(thresh)

    def ave(self):
        if(not self.c_j(0.5)):
            return "cuyo"
            #return self.cuyo()
        if(self.j_a( 0.5)):
            return "jirafa"
            #return self.jirafa()
        if(not self.a_h(0.5)):
            return "avestruz"
        if(self.p_a(0.5)):
            return "pinguino"
            #return self.pinguino()
        
        return "hipopotamo"
        

    def cuyo(self):
        if(self.j_c(0.5) and "J" in self.nodos_usados):
            self.nodos_usados.remove("J")
            return self.jirafa()
        if(self.p_c(0.5) and "P" in self.nodos_usados):
            self.nodos_usados.remove("P")
            return self.pinguino()
        return not self.h_c(0.5)

    def jirafa(self):
        if(self.p_j(0.5) and "P" in self.nodos_usados):
            self.nodos_usados.remove("P")
            return self.pinguino()
        if(self.c_j(0.5) and "C" in self.nodos_usados):
            self.nodos_usados.remove("C")
            return self.j_h(0.5)

    def pinguino(self):
        if(self.j_p(0.5) and "J" in self.nodos_usados):
            self.nodos_usados.remove("J")
            return self.jirafa()
        if(self.c_p(0.5) and "C" in self.nodos_usados):
            self.nodos_usados.remove("C")
            return self.pinguino()
        return "Es un pinguino"
    
    #ave->cuyo->jirafa->pingüino->hipo
    def quienEsEsePokemon(self):
        return self.ave()
           # return "avestruz"
           # return "hipopotamo"
