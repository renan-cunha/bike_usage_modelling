import simpy
from bike_model.bike_model import BikeModel
from station import Station

def get_time(start_time, end_time):
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


    aux = exit_time.copy()
    aux.extend(arrival_time.copy())
    aux.sort()
    times = {}
    b = 0

    for i in aux:
        if i in exit_time:
            times.update({i - b: 'take'})
            b = i
        elif i in arrival_time:
            times.update({i - b: 'arrive'})
            b = i
    return times

while(True):
    x = int(input("\nEntry the sample length:"))
    bikeModel = BikeModel()
    start_time = bikeModel.next_bike_user('start', x)
    end_time = bikeModel.next_bike_user('end', x)

    env = simpy.Environment()
    times = get_time(start_time, end_time)
    estacao = Station(env, 0, 7, times)

    for time, action in times.items():
        env.run()