import Audio2Text
import Video2Audio

def vid2text(filename):
    mp3_file = Video2Audio.vid2audio(filename)
    text_file = Audio2Text.audio2text(mp3_file)
    return text_file

output = vid2text("STEVE_JOBS.mp4")
print(output)