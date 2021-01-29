from simulation import Simulation

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

    simulation = Simulation(bikes, docks-bikes, x)
    results = simulation.start_simulation()

    print("\nNumber of interactions:", results[0])
    print("Withdrawal rate of taking bikes from docks:", results[1])
    print("Withdrawal rate of leaving bikes in docks:", results[2])
            