import re

def divide_speech(long_string):
    # Split the long string into a list of sentences
    sentences = re.split(r'(?<=[.!?]) +', long_string)

    # Initialize a list to store the divided strings
    divided_strings = []

    # Initialize a variable to store the current string
    current_string = ""

    # Initialize a variable to store the word count
    word_count = 0

    # Iterate through the list of sentences
    for sentence in sentences:
        
        # Add the sentence to the current string
        current_string += sentence + " "
        word_count += len(sentence.split())

        # If adding the sentence to the current string would make it have more than 20 words
        if word_count > 20:
            # Add the current string to the list of divided strings
            divided_strings.append(current_string)

            # Reset the current string and word count
            current_string = ""
            word_count = 0


    # if current_string has any remaining words append it to the list
    if len(current_string)>0:
        divided_strings.append(current_string)
    # Return the list of divided strings
    return divided_strings
