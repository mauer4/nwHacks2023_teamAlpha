from google.cloud import language_v1
import Video2Text
from div_speech import *

import sys
import itertools

global speech_txt

def classify(text: str, verbose=True) -> dict:
    """Classify the input text into categories."""

    language_client = language_v1.LanguageServiceClient(client_options={"api_key": "AIzaSyBJQojpSv9yjg2MMXFdy06r0oUIGCjoIs0",
                                                               "quota_project_id": "nwhacks-57419"})

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={"document": document})
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:

        for category in categories:
            print("=" * 20)
            print("{:<16}: {}".format("category", category.name))
            print("{:<16}: {}".format("confidence", category.confidence))

    return result

def getTop(topic: str) -> str:
    """Returns the highest level topic"""

    return topic.split("/")[1]


def combineWeights(main_topics: dict, section_topics: dict):
    """Return dict of topics ordered confidence. Max size 5"""

    for topic in main_topics.keys():
        if topic in section_topics.keys():
            main_topics[topic] = main_topics[topic]*0.5 + section_topics[topic]*0.5
        else:
            main_topics[topic] = main_topics[topic]*0.5

    for topic in section_topics.keys():
        if topic not in main_topics:
            main_topics[topic] = section_topics[topic]*0.5

    # sorts dict based on values
    main_topics = {k: v for k, v in sorted(main_topics.items(), key=lambda item: item[1], reverse=True)}

    return dict(itertools.islice(main_topics.items(), 5))

def analyze_text(filename):
    speech = readFile(filename)
    segments = divide_speech(speech)
    print(len(segments))
    for segment in segments:
        topic_dict = accum_text(segment)
        # Call GUI

def accum_text(text):
    global speech_txt
    d1 = classify(text.strip(), False) if len(text.split(" ")) > 20 else classify(speech_txt.strip(), False)
    speech_txt = speech_txt + " " + text

    #print("\nd1:", d1, "\n")
    #print("\n", speech_txt.strip(), "\n")

    d2 = classify(speech_txt, False)
    #print("\nd2:", d2, "\n")
    x = combineWeights(d1, d2)
    #print("x:", x)
    return x

def readFile(file_path: str) -> str:
    """Read from file specified and return file contents as single line string"""

    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def main():
    global speech_txt
    args = sys.argv[1:]
    speech_txt = ""
    # scrape video file name from cmd and convert to text
    speech_text_file = Video2Text.vid2text(args[0])

    # Analyze speech text file - return sliced dict (size == 5)
    dict = analyze_text(speech_text_file)
    print(dict)

if __name__ == '__main__':
    main()