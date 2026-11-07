import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def extract_audio_from_video(video_path: str, output_path: str):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_path)

def convert_audio_to_wav(input_path: str, output_path: str, target_sr: int = 16000):
    sound = AudioSegment.from_file(input_path)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(target_sr)
    sound.export(output_path, format="wav")
