import simpy
from bike_model.bike_model import BikeModel
from station import Station
from datetime import timedelta

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

while(True):
    x = int(input("\nEntry the simulation time (in hours): "))
    ex = True
    while(ex):
        docks = int(input("\nEntry the number of docks at the station: "))
        bikes = int(input("\nEntry the number of bikes at the station: "))
        if bikes <= docks:
            ex = False
        else:
            print("The number of bikes cannot be greater than the number of docks.")
    time_interval = timedelta(hours=x)
    bikeModel = BikeModel()
    start_time = bikeModel.next_bike_user('start', time_interval)
    end_time = bikeModel.next_bike_user('end', time_interval)

    env = simpy.Environment()
    times = get_time(start_time, end_time)
    estacao = Station(env, docks-bikes, bikes, times)

    print("Number of interactions:", len(times))
    
    for time in times:
        env.run()

# Example
# # start_time = [1,1]
# # end_time = [1,1]
# # times = get_time(start_time, end_time)