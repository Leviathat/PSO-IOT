import random

class Device:
    def __init__(self, device_id, network):
        self.id = device_id
        self.network = network
        self.data = None

    def generate_data(self):
        self.data = random.randint(1, 100)  

    def receive_data(self, data):
        self.data = (self.data + data) / 2

    def send_data(self):
        recipient : Device = random.choice(self.network.devices)
        recipient.receive_data(self.data)


class Network:
    def __init__(self, num_devices):
        self.devices = [Device(i, self) for i in range(num_devices)]

    def run_simulation(self, num_cycles):
        for device in self.devices:
            device.generate_data()

        for _ in range(num_cycles):
            for device in self.devices:
                device.send_data()


