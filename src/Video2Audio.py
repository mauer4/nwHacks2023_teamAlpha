from pydub import AudioSegment

def vid2audio(input_file):

    # File to write the audio to
    output_file = "output.mp3"

    # Load the input file
    audio = AudioSegment.from_file(input_file, format="mp4")

    # Export the audio to the output file
    audio.export(output_file, format="mp3")

    return output_file