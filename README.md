# Video Processing Web Application

## Overview

This project is a web application developed using **Flask** that allows users to upload videos and automatically extract audio and video frames.

The application uses **FFmpeg** for audio extraction and **OpenCV** for extracting video frames at regular intervals.

The extracted audio and frames are saved locally for further processing or analysis.

## Features

- Upload videos through a web interface.
- Extract audio from uploaded videos using FFmpeg.
- Extract video frames using OpenCV.
- Save extracted audio in WAV format.
- Save extracted frames as JPG images.
- Automatically create required directories.
- Display a processing confirmation after successful extraction.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application framework |
| OpenCV | Video frame extraction |
| FFmpeg | Audio extraction |
| HTML | Frontend interface |

## Project Structure

```text
Video-Processing-Project/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
│       └── uploaded_video.mp4
│
├── extracted/
│   ├── frames/
│   │   ├── frame0.jpg
│   │   ├── frame1.jpg
│   │   └── ...
│   │
│   └── audio.wav
│
└── README.md
```

### Directory Description

- `app.py`: Main Flask application.
- `templates/index.html`: HTML page containing the video upload interface.
- `static/uploads/`: Stores uploaded videos.
- `extracted/frames/`: Stores extracted video frames.
- `extracted/audio.wav`: Stores the audio extracted from the uploaded video.

The upload and frame directories are automatically created when the application starts.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Video-Processing-Project
```

### 2. Install Python Dependencies

Make sure Python is installed on your system.

Install the required Python libraries:

```bash
pip install flask opencv-python ffmpeg-python
```

### 3. Install FFmpeg

FFmpeg must be installed separately because the Python `ffmpeg-python` package is only a wrapper around the FFmpeg executable.

Download FFmpeg from:

https://ffmpeg.org/download.html

After installation, ensure FFmpeg is added to your system PATH.

Verify the installation:

```bash
ffmpeg -version
```

### 4. Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally at:

http://127.0.0.1:5000/

Open this URL in your browser to access the application.

## Application Workflow

The application follows these steps:

1. The user opens the web application.
2. The user selects and uploads a video file.
3. Flask receives the uploaded video through the `/upload` endpoint.
4. The uploaded video is saved in `static/uploads/`.
5. FFmpeg extracts the audio and saves it as `extracted/audio.wav`.
6. OpenCV reads the video and extracts frames at approximately one-second intervals.
7. Extracted frames are saved in `extracted/frames/`.
8. The application returns a confirmation message containing the extraction locations.

## Routes

### Home Route

**Endpoint:** `/`

**Method:** GET

Displays the main webpage using the `index.html` template.

```python
@app.route('/')
def index():
    return render_template('index.html')
```

### Video Upload Route

**Endpoint:** `/upload`

**Method:** POST

Receives the uploaded video and initiates audio and frame extraction.

The endpoint:

- Checks whether a video file was uploaded.
- Saves the uploaded video.
- Calls the audio extraction function.
- Calls the frame extraction function.
- Returns a processing confirmation.

If no video file is provided, the application returns a `400 Bad Request` response.

## Audio Extraction

Audio extraction is performed using FFmpeg.

```python
def extract_audio_ffmpeg(video_path, audio_output):
    ffmpeg.input(video_path).output(audio_output).run(
        overwrite_output=True
    )
```

The function:

- Takes the uploaded video path as input.
- Extracts the audio stream.
- Saves the extracted audio to the specified output path.
- Overwrites the existing output file if necessary.

**Output:** `extracted/audio.wav`

## Video Frame Extraction

Video frames are extracted using OpenCV.

```python
def extract_frames_opencv(video_path, output_folder):
```

The function:

1. Opens the video using `cv2.VideoCapture()`.
2. Retrieves the video's frame rate.
3. Reads frames sequentially.
4. Extracts one frame approximately every second.
5. Saves each extracted frame as a JPG image.
6. Releases the video capture resource after processing.

### Frame Extraction Logic

The application uses the following condition:

```python
if count % fps == 0:
```

This extracts one frame for every `fps` frames processed.

For example, if the video has a frame rate of 30 FPS, the application extracts approximately one frame every 30 frames, corresponding to approximately one second.

Extracted frames are named sequentially:

```text
frame0.jpg
frame1.jpg
frame2.jpg
...
```

## Output

After processing, the application generates the following outputs:

| Output | Location |
|---|---|
| Uploaded video | `static/uploads/` |
| Extracted audio | `extracted/audio.wav` |
| Extracted frames | `extracted/frames/` |

The application returns a confirmation message indicating where the audio and frames have been saved.

## Future Enhancements

Possible improvements include:

- Display extracted frames directly on the webpage.
- Add a download option for the extracted audio.
- Allow users to download extracted frames as a ZIP file.
- Add video duration and frame rate information.
- Support multiple video formats.
- Add progress indicators during processing.
- Implement file validation and upload size limits.
- Support selecting custom frame extraction intervals.
- Add automatic cleanup of previously uploaded files.
- Improve error handling for invalid or unsupported videos.

## Author

Developed as a Python-based video processing project using Flask, FFmpeg, and OpenCV.
