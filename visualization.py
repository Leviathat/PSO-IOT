import matplotlib.pyplot as plt

def plot_data(data, labels=None):
    plt.figure(figsize=(10, 6))
    if labels:
        plt.plot(data, label=labels)
    else:
        plt.plot(data)
    plt.xlabel("Time Step")
    plt.ylabel("Data Value")
    plt.title("Simulated IoT Network Data")
    plt.grid(True)
    plt.show()

def plot_anomaly(data, anomaly_index, anomaly_value):
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.axvline(x=anomaly_index, color='red', linestyle='dashed', linewidth=2, label='Anomaly Detected')
    plt.scatter(anomaly_index, anomaly_value, color='red', s=100, label='Anomaly Value')
    plt.xlabel("Time Step")
    plt.ylabel("Data Value")
    plt.title("Simulated IoT Network Data with Anomaly Detection")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_metrics(metrics, labels):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, metrics)
    plt.xlabel("Metric")
    plt.ylabel("Value")
    plt.title("Swarm Intelligence Metrics")
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

