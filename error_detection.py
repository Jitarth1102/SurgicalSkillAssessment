class ErrorDetector:
    def __init__(self, deviation_threshold=10):
        self.deviation_threshold = deviation_threshold

    def detect_errors(self, tool_positions, expected_path):
        """
        Detect errors based on large deviations from the expected path.
        """
        errors_detected = []
        for pos, exp_pos in zip(tool_positions, expected_path):
            if pos is not None and exp_pos is not None:
                deviation = np.linalg.norm(np.array(pos) - np.array(exp_pos))
                if deviation > self.deviation_threshold:
                    errors_detected.append(True)
                else:
                    errors_detected.append(False)
        
        return errors_detected
