import argparse
import io
import json
import os

from google.cloud import language_v1
import numpy
import six

def classify(text, verbose=True):
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
