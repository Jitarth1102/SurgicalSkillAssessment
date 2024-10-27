import matplotlib.pyplot as plt

class PerformanceTracker:
    def __init__(self):
        self.performance_log = []

    def log_performance(self, surgeon_id, score, date):
        """
        Log the performance of a surgeon.
        """
        self.performance_log.append({
            'surgeon_id': surgeon_id,
            'score': score,
            'date': date
        })

    def visualize_trend(self):
        """
        Visualize the trend of performance over time.
        """
        dates = [entry['date'] for entry in self.performance_log]
        scores = [entry['score'] for entry in self.performance_log]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, scores, marker='o', linestyle='-')
        plt.title('Performance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Score')
        plt.grid(True)
        plt.show()
