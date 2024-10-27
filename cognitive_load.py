class CognitiveLoadMonitor:
    def __init__(self, device=None):
        """
        Initialize the cognitive load monitor.
        The device parameter could simulate a wearable or other data collection device.
        """
        self.device = device

    def get_load_metrics(self):
        """
        Get the cognitive load metrics.
        In a real-world scenario, this might collect physiological data (heart rate, etc.).
        """
        # Simulated cognitive load value
        cognitive_load = 0.3  # Value between 0 and 1 (0: no load, 1: maximum load)
        return cognitive_load
