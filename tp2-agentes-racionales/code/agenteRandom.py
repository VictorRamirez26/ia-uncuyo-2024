import agente
import random

class AgenteRandom(agente.Agent):
    def __init__(self, env):
        super().__init__(env)

    def clean(self):
        if self.suck():
            self.performance += 1

    def randomMov(self):
        randomMov = random.randint(0,5) 
        if randomMov == 0:
            self.up()
        elif randomMov == 1:
            self.down()
        elif randomMov == 2:
            self.left()
        elif randomMov == 3:
            self.right()   
        elif randomMov == 4: 
            self.clean()
        else:
            self.idle()

    def think(self):
        necessaryMoves = 0
        while self.mov != 0:
            if self.env.get_dirty() != 0:
                necessaryMoves += 1 # Movimientos necesarios para limpiar las casillas
            self.randomMov()
            self.mov -= 1
        return self.performance , necessaryMoves 