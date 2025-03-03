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
        
    def get_leave_withdrawal(self):
        return self.leave_bike_withdrawal

    def get_take_withdrawal(self):
        return self.take_bike_withdrawal

    def run(self):
        for _time in self.times:
            if _time[1] == 'arrive':
                if self.docks_slots == 0:
                    self.leave_bike_withdrawal += 1
                else:
                    self.docks_slots -= 1
                    self.bikes_slots += 1
                    yield self.env.timeout(_time[0])
            elif _time[1] == 'take':
                if self.bikes_slots == 0:
                    self.take_bike_withdrawal += 1
                else:
                    self.docks_slots += 1
                    self.bikes_slots -= 1
                    yield self.env.timeout(_time[0])