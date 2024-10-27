import pandas as pd
import cv2
import os

def load_m2cai_annotations(annotation_path):
    """
    Load M2CAI workflow annotations, which include timestamps and phases.
    """
    annotations = pd.read_csv(annotation_path)
    annotations['StartTime'] = pd.to_datetime(annotations['StartTime'], format='%H:%M:%S')
    annotations['EndTime'] = pd.to_datetime(annotations['EndTime'], format='%H:%M:%S')
    return annotations

def load_cholec80_annotations(annotation_dir):
    """
    Load Cholec80 phase annotations, which include phase labels and timestamps for each surgery.
    """
    annotation_files = [f for f in os.listdir(annotation_dir) if f.endswith('.txt')]
    cholec80_annotations = []
    
    for file in annotation_files:
        annotations = pd.read_csv(os.path.join(annotation_dir, file), delimiter=' ', header=None)
        annotations.columns = ['Time', 'Phase']
        cholec80_annotations.append(annotations)
    
    return cholec80_annotations

def preprocess_video(video_path):
    """
    Load video file and return frames. Frames will be processed later for tool tracking.
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()
    return frames
