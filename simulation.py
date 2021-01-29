import simpy
from bike_model.bike_model import BikeModel
from station import Station
from datetime import timedelta

class Simulation:

    def __init__(self, available_bikes: int, available_docks: int, simulation_time: int):
        self.available_bikes = available_bikes
        self.available_docks = available_docks
        self.simulation_time = simulation_time
        
    def get_time(self, start_time: list, end_time: list) -> list:
        exit_time = []
        arrival_time = []

        for i in range(len(start_time)):
            if i == 0:
                exit_time.append(start_time[i])
            else:
                exit_time.append(start_time[i] + exit_time[i-1])
        
        for i in range(len(end_time)):
            if i == 0:
                arrival_time.append(end_time[i])
            else:
                arrival_time.append(end_time[i] + arrival_time[i-1])

        aux = []
        for i in exit_time:
            aux.append((i, 'take'))

        for i in arrival_time:
            aux.append((i, 'arrive'))
        
        aux.sort()
        times = []
        
        j = 0
        for i in aux:
            if i[1] == 'take':
                times.append((i[0] - j, 'take'))
                j = i[0]
            if i[1] == 'arrive':
                times.append((i[0] - j, 'arrive'))
                j = i[0]
        return times
        
    def start_simulation(self) -> list:
        time_interval = timedelta(hours=self.simulation_time)
        bikeModel = BikeModel()
        start_time = bikeModel.next_bike_user('start', time_interval)
        end_time = bikeModel.next_bike_user('end', time_interval)

        env = simpy.Environment()
        times = self.get_time(start_time, end_time)
        self.station = Station(env, self.available_docks, self.available_bikes, times)
        
        for _ in times:
            env.run()

        return [len(times), self.station.get_take_withdrawal(), self.station.get_leave_withdrawal()]