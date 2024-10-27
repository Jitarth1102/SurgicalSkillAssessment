import cv2
import numpy as np

class ToolTracker:
    def __init__(self):
        self.tracker_type = 'KCF'  # Use KCF (Kernelized Correlation Filter) tracker for tool tracking
        self.tracker = cv2.TrackerKCF_create()

    def initialize_tracker(self, first_frame, bbox):
        """
        Initialize the tracker with the bounding box (bbox) around the surgical tool in the first frame.
        """
        self.tracker.init(first_frame, bbox)
    
    def track_tool(self, video_frames):
        """
        Track the surgical tool across the video frames.
        """
        tool_positions = []

        for frame in video_frames:
            success, bbox = self.tracker.update(frame)
            if success:
                # Append the center of the bbox as the tool position
                tool_positions.append(((bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2))
            else:
                tool_positions.append(None)

        return tool_positions

    def calculate_smoothness(self, tool_positions):
        """
        Calculate smoothness based on the positional changes of the tool over time.
        """
        smoothness_scores = []
        for i in range(1, len(tool_positions)):
            if tool_positions[i] is not None and tool_positions[i-1] is not None:
                diff = np.linalg.norm(np.array(tool_positions[i]) - np.array(tool_positions[i-1]))
                smoothness_scores.append(diff)
        
        # A lower average diff implies smoother movements
        smoothness = np.mean(smoothness_scores) if smoothness_scores else float('inf')
        return smoothness
