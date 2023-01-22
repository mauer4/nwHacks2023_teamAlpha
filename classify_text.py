from google.cloud import language_v1
import itertools

speech_txt = ""

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
    remaining_topics = {k: v for k, v in sorted(remaining_topics.items(), key=lambda item: item[1], reverse=True)}

    return dict(itertools.islice(main_topics.items(), 5))

def main():
    print("d1")
    d1 = classify("Technology is a rapidly evolving field that encompasses a wide range of products, services, and processes. From smartphones and laptops to the internet and artificial intelligence, technology has had a profound impact on the way we live, work, and communicate. Advances in computing power, storage capacity, and networking have enabled new breakthroughs in areas such as big data, machine learning, and the Internet of Things.")
    print("\nd2\n")
    d2 = classify("In addition, technology has also played a key role in driving innovation and economic growth, creating new industries and jobs, and improving productivity and efficiency. However, with these benefits also come challenges, such as cybersecurity threats, privacy concerns, and the impact of technology on society and the workforce. Overall, technology will continue to be a driving force in shaping the future, and it is important for individuals and organizations to stay informed and adapt to the latest developments in order to stay competitive and take advantage of the many opportunities it offers.")
    print("")
    x = combineWeights(d1, d2)
    print(x)
main()

def analyze_text(filename):
    with open(filename, "rw") as speech:
        
    

def accum_text(text):
    speech_txt += " " + text
    d1 = classify(text)
    d2 = classify(speech_txt)
    x = combineWeights(d1, d2)