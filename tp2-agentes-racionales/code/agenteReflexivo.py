import agente
import random
class AgenteReflexivo(agente.Agent):
    def __init__(self, env):
        super().__init__(env)
    
    def perspective(self): # sensa el entorno
        return self.env.is_dirty(self.posX,self.posY)

    def clean(self):
        self.suck()
        self.performance += 1

    def randomMov(self):
        randomMov = random.randint(0,3) 
        if randomMov == 0:
            self.up()
        elif randomMov == 1:
            self.down()
        elif randomMov == 2:
            self.left()
        else:
            self.right()   
        # Por el momento no tomo el idle como movimiento
        ##else: 
            ##self.idle()

    def think(self):
        necessaryMoves = 1000
        while self.mov != 0:
            if self.perspective(): # Verifico si la casilla esta sucia
                self.clean()
                if self.env.get_dirty() == 0:
                    necessaryMoves = 1000 - self.mov # Movimientos necesarios para limpiar las casillas
            else:
                self.randomMov()
            self.mov -= 1
        return self.performance , necessaryMoves 
