from iot_network import Network
from swarm_intelligence import Swarm
from visualization import plot_data, plot_anomaly, plot_metrics
from collections import deque


num_devices = 5
num_cycles = 10
threshold = 90
num_particles = 10

fitness_history = deque(maxlen=num_cycles)  
convergence_rate = None

network = Network(num_devices)
data = []  
for _ in range(num_cycles):
    network.run_simulation(1)
    for device in network.devices:
        data.append(device.data)

swarm = Swarm(num_particles, data, threshold)
for _ in range(num_cycles): 
    swarm.update()
    anomaly_index, anomaly_value = swarm.get_anomaly()  

if len(fitness_history) > 1:
    convergence_rate = (fitness_history[0] - fitness_history[-1]) / fitness_history[0]

plot_data(data)
plot_anomaly(data, anomaly_index, anomaly_value)
#plot_anomaly(data, anomaly_index, anomaly_value)
