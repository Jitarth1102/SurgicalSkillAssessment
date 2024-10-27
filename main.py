from data_preparation import parse_phase_annotations, parse_tool_annotations, extract_frames_from_video
from tool_tracking import ToolTracker
from cognitive_load import CognitiveLoadMonitor
from error_detection import ErrorDetector
from performance_tracking import PerformanceTracker
from scoring_system import ScoringSystem

def main():
    # Define file paths
    video_file = './cholec80/videos/video01.mp4'
    timestamp_file = './cholec80/videos/video01-timestamp.txt'
    phase_file = './cholec80/phase_annotations/video01-phase.txt'
    tool_file = './cholec80/tool_annotations/video01-tool.txt'

    # Parse the annotations
    phase_annotations = parse_phase_annotations(phase_file)
    tool_annotations = parse_tool_annotations(tool_file)

    # Extract frames from the video based on the timestamp file
    frames = extract_frames_from_video(video_file, timestamp_file)

    # Initialize components
    tool_tracker = ToolTracker()
    cognitive_monitor = CognitiveLoadMonitor()
    error_detector = ErrorDetector()
    scoring_system = ScoringSystem()
    performance_tracker = PerformanceTracker()

    # Track tools and calculate metrics
    tool_positions = tool_tracker.track_tools(frames)
    smoothness = tool_tracker.calculate_smoothness(tool_positions)

    # Evaluate performance for each phase
    final_score = 0
    expected_duration = 300  # Dummy expected duration for each phase
    for frame_number, frame in frames:
        phase = phase_annotations.get(frame_number, "Unknown")
        efficiency = scoring_system.calculate_efficiency(len(frames), expected_duration)
        precision = scoring_system.calculate_precision(tool_positions, tool_annotations)
        cognitive_load = cognitive_monitor.get_load_metrics()

        performance_metrics = {
            'efficiency': efficiency,
            'precision': precision,
            'smoothness': smoothness,
            'cognitive_load': cognitive_load
        }

        score = scoring_system.assign_score(phase, performance_metrics)
        final_score += score

    # Log performance and visualize
    surgeon_id = 1
    performance_tracker.log_performance(surgeon_id, final_score, "2024-10-18")
    performance_tracker.visualize_trend()

    print(f'Final Surgical Skill Score: {final_score}')

if __name__ == "__main__":
    main()
