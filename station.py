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
            if tag == 'arrive':
                if self.docks_slots == 0:
                    self.leave_bike_withdrawal += 1
                    print("Gave up leaving the bike at {0} seconds".format(self.env.now))
                else:
                    self.docks_slots -= 1
                    self.bikes_slots += 1
                    yield self.env.timeout(_time)
                    print("Bike arrived at {0} seconds".format(self.env.now))
            elif tag == 'take':
                if self.bikes_slots == 0:
                    self.take_bike_withdrawal += 1
                    print("Gave up taking the bike at {0} seconds".format(self.env.now))
                else:
                    self.docks_slots += 1
                    self.bikes_slots -= 1
                    yield self.env.timeout(_time)
                    print("Bike left at {0} seconds".format(self.env.now))
        print("\nWithdrawal rate of leaving bikes in docks: {0}".format(self.leave_bike_withdrawal))
        print("Withdrawal rate of taking bikes from docks: {0}".format(self.take_bike_withdrawal))