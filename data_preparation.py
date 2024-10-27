import cv2

def parse_phase_annotations(phase_file):
    """
    Parse the phase annotations file.
    Returns a dictionary with frame number as keys and the corresponding phase as values.
    """
    phase_annotations = {}
    with open(phase_file, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header
        for line in lines:
            frame, phase = line.strip().split('\t')
            phase_annotations[int(frame)] = phase  # Store phase for each frame
    return phase_annotations

def parse_tool_annotations(tool_file):
    """
    Parse the tool annotations file.
    Returns a dictionary with frame number as keys and tool usage as values.
    """
    tool_annotations = {}
    with open(tool_file, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header
        for line in lines:
            values = line.strip().split('\t')
            frame = int(values[0])
            tools = list(map(int, values[1:]))  # Tool usage as a list of binary values
            tool_annotations[frame] = tools
    return tool_annotations

def extract_frames_from_video(video_file, timestamp_file):
    """
    Extract frames from the video at given timestamps.
    Returns a list of frames and their corresponding frame numbers.
    """
    cap = cv2.VideoCapture(video_file)
    timestamps = []
    
    # Parse the timestamp file to get the frames to extract
    with open(timestamp_file, 'r') as f:
        lines = f.readlines()[1:]  # Skip the header
        for line in lines:
            timestamp = line.strip().split('\t')[0]
            # Convert timestamp to seconds
            h, m, s = map(float, timestamp.split(':'))
            total_seconds = int(h * 3600 + m * 60 + s)
            timestamps.append(total_seconds)

    frames = []
    for timestamp in timestamps:
        cap.set(cv2.CAP_PROP_POS_FRAMES, timestamp)
        ret, frame = cap.read()
        if ret:
            frames.append((timestamp, frame))  # Store frame number and frame data
    
    cap.release()
    return frames
