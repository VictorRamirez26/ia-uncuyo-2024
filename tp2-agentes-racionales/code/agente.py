from abc import ABC, abstractmethod
import random
class Agent(ABC):
    def __init__(self,env): # recibe como parametro un objeto de la clase Environment
        self.env = env
        self.posX = random.randint(0,self.env.posX-1)
        self.posY = random.randint(0,self.env.posY-1)
        self.performance = 0 # Cantidad de casillas limpiadas
        self.mov = 1000 # Cantidad de acciones iniciales
        
    def up(self):
        if self.env.acceptAction("Arriba", self.posX , self.posY):
            self.posX += 1
        return
        
    def down(self):
        if self.env.acceptAction("Abajo", self.posX , self.posY):
            self.posX -= 1
        return
        
    def left(self):
        if self.env.acceptAction("Izquierda", self.posX , self.posY):
            self.posY -= 1       
        return    
    def right(self):
        if self.env.acceptAction("Derecha", self.posX , self.posY):
            self.posY += 1
        return
    
    def suck(self): # Limpia
        return self.env.acceptAction("Limpiar", self.posX , self.posY)
        
    def idle(self): # no hace nada
        return
    
    def perspective(self,env): # sensa el entorno
        return
    
    @abstractmethod
    def think(self):
        pass  # Método abstracto, debe ser implementado por las subclases (Agente reflexivo simple y agente aleatorio)