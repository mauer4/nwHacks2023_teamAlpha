import Audio2Text
import Video2Audio

def vid2text(filename="obama.mp4"):
    mp3_file = Video2Audio.vid2audio(filename)
    text_file = Audio2Text.audio2text(mp3_file)
    return text_file

vid2text()