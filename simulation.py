import simpy
import numpy as np
from bike_model.bike_model import BikeModel

bikeModel = BikeModel()
start_time = bikeModel.next_bike_user('start', size=20)
end_time = bikeModel.next_bike_user('end', size=20)

env = simpy.Environment()
docks = simpy.Resource(env, capacity=2)


""""
import simpy

def supermarket(env, name, line, arriveTime, serviceTime):
	yield env.timeout(arriveTime)
	print('%s arriving at %d' %(name, env.now))

	with line.request() as req:
		yield req

		print('%s being attended at %s' %(name, env.now))
		yield env.timeout(serviceTime)
		print('%s leaving the supermarket at %s' %(name, env.now))


env = simpy.Environment()
line = simpy.Resource(env, capacity=1)
arriveTime = [0, 1, 1, 2]
serviceTime = [3, 4, 6, 4]

for i in range(4):
	env.process(supermarket(env, 'Client %d' %(i+1), line, arriveTime[i], serviceTime[i]))

env.run()
"""