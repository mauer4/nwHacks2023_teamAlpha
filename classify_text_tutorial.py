import argparse
import io
import json
import os

from google.cloud import language_v1
import numpy
import six

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

    result: dict = {}
    for topic in main_topics.keys():
        if topic in section_topics.keys():
            result[topic] = main_topics[topic]*0.5 + section_topics[topic]*0.5

    if len(result) < 5:
        remaining_topics: dict = {}
        for topic in main_topics.keys():
            if topic not in result.keys():
                remaining_topics[topic] = main_topics[topic]

        for topic in section_topics.keys():
            if topic not in result.keys():
                remaining_topics[topic] = section_topics[topic]

        # sorts dict based on values
        remaining_topics = {k: v for k, v in sorted(remaining_topics.items(), key=lambda item: item[1])}

        for i in range(5-len(result)):
            if i < len(remaining_topics):
                result[list(remaining_topics.keys())[i]] = remaining_topics[list(remaining_topics.keys())[i]]
    else:
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

    return result