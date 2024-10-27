from data_preparation import load_m2cai_annotations, load_cholec80_annotations, preprocess_video
from tool_tracking import ToolTracker
from scoring_system import ScoringSystem
from error_detection import ErrorDetector

def main():
    # Load annotations and videos
    m2cai_annotations = load_m2cai_annotations('m2cai_annotations.csv')
    cholec80_annotations = load_cholec80_annotations('cholec80_annotations_dir')
    video_frames = preprocess_video('surgery_video.mp4')

    # Initialize components
    tool_tracker = ToolTracker()
    scoring_system = ScoringSystem()
    error_detector = ErrorDetector()

    # Tracking tools and calculating metrics
    bbox = (50, 50, 100, 100)  # Example initial bounding box for tool
    tool_tracker.initialize_tracker(video_frames[0], bbox)
    tool_positions = tool_tracker.track_tool(video_frames)
    smoothness_score = tool_tracker.calculate_smoothness(tool_positions)

    # Evaluate performance for each phase
    final_score = 0
    for phase in cholec80_annotations:
        phase_name = phase['Phase'].iloc[0]
        phase_duration = len(phase)  # Number of frames in the phase
        
        # Define expected path (mockup for illustration)
        expected_path = [(50 + i, 50 + i) for i in range(len(phase))]

        precision_score = scoring_system.calculate_precision(tool_positions[:phase_duration], expected_path)
        efficiency_score = scoring_system.calculate_efficiency(phase_duration, expected_duration=300)
        
        performance_metrics = {
            'precision': precision_score,
            'efficiency': efficiency_score,
            'smoothness': smoothness_score,
        }
        
        phase_score = scoring_system.assign_score(phase_name, performance_metrics)
        final_score += phase_score

    print(f"Final Surgery Score: {final_score}")

if __name__ == '__main__':
    main()
