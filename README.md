### nwHacks2023_teamAlpha
Speech video analytics

Takes a video of individual speech, and creates a visual feedback window that shows you throughout the video what topic the speaker was talking about. The more topic exist, the less focus there is in the speech.  The graphical user interface is a tree graph the is labeled with topics and keeps the most dominant topic in the speech at the top lane of the tree.

## ML model used locally:
openai-whisper

## API used:
gcloud-NLP (google)

## Dependencies:
- google.cloud
- tkinter
- ffmpeg
- pytorch
- pydub

## Data flow - input is path to .mp4:
.mp4 -> .mp3 -> .txt -> Data Analysis -> GUI

to run with all dependencies run:
`python3 classify_text.py <filepath/filename.mp4>`

obama.mp4 given in directory


<img width="720" alt="image" src="https://user-images.githubusercontent.com/89616796/213937523-12fb6fe2-6a02-4143-ab42-ead703db2c5d.png">
