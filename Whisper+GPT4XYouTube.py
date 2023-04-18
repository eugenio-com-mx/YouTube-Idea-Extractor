import pytube
import youtube_dl
import moviepy.editor as mp
import whisper
import ffmpeg
import tiktoken
import random
import numpy as np

video_url = "https://www.youtube.com/watch?v=QWtI4WQrfC8"  # Replace with your desired YouTube video URL

MAX_AUDIO_FILE_SIZE = 25 * 1024 * 1024
SEGMENT_DURATION = 1800

def download_audio(video_url): 
    data = pytube.YouTube(video_url)
    audio = data.streams.get_audio_only()
    downloaded_file = audio.download()
    return downloaded_file

input_file = download_audio(video_url)

output_file = "audio.wav"

def convert_audio(input_file, output_file):
    audio = mp.AudioFileClip(input_file)
    audio.write_audiofile(output_file, codec="pcm_s16le")

convert_audio(input_file, output_file)

from whisper import Whisper

whisper_model = Whisper("base.en")  # Load the ASR model
result = whisper_model.transcribe("audio.wav")
print(result["text"])