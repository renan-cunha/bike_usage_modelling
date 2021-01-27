import simpy

class Station:
    def __init__(self, env, docks_slots, bikes_slots, times):
        self.env = env
        self.docks_slots = docks_slots
        self.bikes_slots = bikes_slots
        self.take_bike_withdrawal = 0
        self.leave_bike_withdrawal = 0
        self.times = times
        self.env.process(self.run())
        
    def run(self):
        for _time, tag in self.times.items():
            if tag == 'chegada':
                if self.docks_slots == 0:
                    self.leave_bike_withdrawal += 1
                    print("Desistiu de deixar a bike na dock no tempo", self.env.now)
                else:
                    self.docks_slots -= 1
                    self.bikes_slots += 1
                    yield self.env.timeout(_time)
                    print("Bike chegou no tempo", self.env.now)
            elif tag == 'retirada':
                if self.bikes_slots == 0:
                    self.take_bike_withdrawal += 1
                    print("Desistiu de retirar a bike da dock no _time", self.env.now)
                else:
                    self.docks_slots += 1
                    self.bikes_slots -= 1
                    yield self.env.timeout(_time)
                    print("Bike saiu no _time", self.env.now)
        print("Quantidade de desistências para deixar a bike na dock:", self.leave_bike_withdrawal)
        print("Quantidade de desistências para retirar a bike da dock:", self.take_bike_withdrawal)
