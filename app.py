from flask import Flask, request, render_template
import os
import cv2
import ffmpeg

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
FRAME_FOLDER = 'extracted/frames'
AUDIO_OUTPUT = 'extracted/audio.wav'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(FRAME_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No video uploaded', 400

    video = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    extract_audio_ffmpeg(video_path, AUDIO_OUTPUT)
    extract_frames_opencv(video_path, FRAME_FOLDER)

    return f"Processed! Audio: {AUDIO_OUTPUT}, Frames: {FRAME_FOLDER}"

def extract_audio_ffmpeg(video_path, audio_output):
    # Use ffmpeg to extract audio
    ffmpeg.input(video_path).output(audio_output).run(overwrite_output=True)

def extract_frames_opencv(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    count = 0
    frame_num = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % fps == 0:
            frame_path = os.path.join(output_folder, f"frame{frame_num}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_num += 1
        count += 1

    cap.release()

if __name__ == '__main__':
    app.run(debug=True)
