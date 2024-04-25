import random
import numpy as np

class Particle:
    def __init__(self, position):
        self.position = position
        self.best_position = position
        self.best_fitness = float('inf')  

    def update(self, data, threshold):
        fitness = self.calculate_fitness(data, threshold)

        if fitness < self.best_fitness:
            self.best_position = self.position
            self.best_fitness = fitness

    def calculate_fitness(self, data, threshold):
        
        average = sum(data) / len(data)
        std_dev = np.std(data)  

        
        deviations = [abs(d - average) for d in data if abs(d - average) > threshold * std_dev]

       
        fitness = sum(deviations) * len(deviations)  
        return fitness


class Swarm:
    def __init__(self, num_particles, data, threshold):
        self.particles = [Particle([random.uniform(0, 1) for _ in range(len(data))])
                          for _ in range(num_particles)]
        self.data = data
        self.threshold = threshold
        self.gbest_position = None
        self.gbest_fitness = float('inf')

    def update(self):
        for particle in self.particles:
            particle.update(self.data, self.threshold)

            
            if particle.best_fitness > self.gbest_fitness:
                self.gbest_position = particle.best_position
                self.gbest_fitness = particle.best_fitness

    def get_anomaly(self):
        
        max_deviation_index = np.argmax(self.gbest_position)
        return max_deviation_index, self.data[max_deviation_index]


