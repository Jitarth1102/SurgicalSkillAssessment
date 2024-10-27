class ScoringSystem:
    def __init__(self):
        self.scores = {}

    def calculate_efficiency(self, phase_duration, expected_duration):
        """
        Calculate efficiency based on the duration of each phase relative to expected durations.
        """
        efficiency_score = max(0, 1 - (phase_duration / expected_duration))
        return efficiency_score

    def calculate_precision(self, tool_positions, expected_path):
        """
        Compare tool positions with expected paths for the task and calculate precision.
        """
        total_deviation = 0
        for pos, exp_pos in zip(tool_positions, expected_path):
            if pos is not None and exp_pos is not None:
                deviation = np.linalg.norm(np.array(pos) - np.array(exp_pos))
                total_deviation += deviation

        precision_score = 1 / (1 + total_deviation)  # Inverse relationship between deviation and score
        return precision_score

    def assign_score(self, phase, performance_metrics):
        """
        Assign an overall score based on phase complexity and performance metrics (precision, efficiency).
        """
        phase_complexity = self.get_phase_complexity(phase)
        efficiency = performance_metrics['efficiency']
        precision = performance_metrics['precision']
        smoothness = performance_metrics['smoothness']
        
        total_score = (efficiency * 0.4 + precision * 0.4 + smoothness * 0.2) * phase_complexity
        return total_score

    def get_phase_complexity(self, phase):
        """
        Define a complexity score for each phase. Complex phases contribute more to the final score.
        """
        complexity_map = {
            "Preparation": 0.5,
            "Calot Triangle Dissection": 1.5,
            "Clipping and Cutting": 1.2,
            "Gallbladder Dissection": 1.8,
            "Gallbladder Packaging": 0.8,
            "Cleaning": 0.7,
            "Final Inspection": 0.6,
        }
        return complexity_map.get(phase, 1.0)  # Default complexity is 1.0
