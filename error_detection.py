import numpy as np

class ErrorDetector:
    def __init__(self, deviation_threshold=10):
        self.deviation_threshold = deviation_threshold

    def detect_errors(self, tool_positions, expected_path):
        """
        Detect errors based on large deviations from the expected path.
        Returns a list of frames where errors were detected.
        """
        errors_detected = []
        for frame_number, position in tool_positions.items():
            expected_position = expected_path.get(frame_number, (100, 100))  # Dummy expected path
            deviation = np.linalg.norm(np.array(position) - np.array(expected_position))
            if deviation > self.deviation_threshold:
                errors_detected.append(frame_number)
        return errors_detected
