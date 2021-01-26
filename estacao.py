import simpy

class Estacao:
    def __init__(self, env, docks_vagas, bikes_vagas, tempos):
        self.env = env
        self.docks_vagas = docks_vagas
        self.bikes_vagas = bikes_vagas
        self.desistencias_retirar = 0
        self.desistencias_deixar = 0
        self.tempos = tempos
        self.env.process(self.run())
        
    def run(self):
        for tempo, rotulo in self.tempos.items():
            if rotulo == 'chegada':
                if self.docks_vagas == 0:
                    self.desistencias_deixar += 1
                    print("Desistiu de deixar a bike na dock no tempo", self.env.now)
                else:
                    self.docks_vagas -= 1
                    self.bikes_vagas += 1
                    yield self.env.timeout(tempo)
                    print("Bike chegou no tempo", self.env.now)
            elif rotulo == 'retirada':
                if self.bikes_vagas == 0:
                    self.desistencias_retirar += 1
                    print("Desistiu de retirar a bike da dock no tempo", self.env.now)
                else:
                    self.docks_vagas += 1
                    self.bikes_vagas -= 1
                    yield self.env.timeout(tempo)
                    print("Bike saiu no tempo", self.env.now)
        print("Taxa de desistência para deixar a bike na dock:", self.desistencias_deixar)
        print("Taxa de desistência para retirar a bike da dock:", self.desistencias_retirar)
