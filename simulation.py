import simpy
import numpy as np
from bike_model.bike_model import BikeModel
from estacao import Estacao

bikeModel = BikeModel()
start_time = bikeModel.next_bike_user('start', size=10)
end_time = bikeModel.next_bike_user('end', size=10)

tempos_de_saida = []
tempos_de_chegada = []

for i in range(len(start_time)):
    if i == 0:
        tempos_de_saida.append(start_time[i])
    else:
        tempos_de_saida.append(start_time[i] + tempos_de_saida[i-1])

for i in range(len(end_time)):
    if i == 0:
        tempos_de_chegada.append(end_time[i])
    else:
        tempos_de_chegada.append(end_time[i] + tempos_de_chegada[i-1])


aux = tempos_de_saida.copy()
aux.extend(tempos_de_chegada.copy())
aux.sort()
tempos = {}
b = 0

for i in aux:
    if i in tempos_de_saida:
        tempos.update({i - b: 'retirada'})
        b = i
    elif i in tempos_de_chegada:
        tempos.update({i - b: 'chegada'})
        b = i

env = simpy.Environment()
estacao = Estacao(env, 0, 7, tempos)

for tempo, acao in tempos.items():
    env.run()