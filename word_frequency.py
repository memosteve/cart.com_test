import sys
import re

# Remove punctuation, numbers, and convert to lowercase for counting all the words
def clean_text(text):
    text = re.sub(r'\b\d+\b', '', text)  
    text = re.sub(r'[\W_]+', ' ', text)
    return text.lower()

def word_frequency(file_path):
    # Open and read the file 
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return

    if not text.strip():
        print("The file is empty.")
        return

    # Call the function clean_text and convert the text into an array of words
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    # Use lists to store frequencies for each word and original words
    single_word_list = []
    original_words = []

    for word in re.findall(r'\b\w+\b', text):
        cleaned_word = word.lower()
        if cleaned_word and not cleaned_word.isdigit():
            if cleaned_word not in single_word_list:
                single_word_list.append(cleaned_word)
                original_words.append(word)
            else:
                original_words[single_word_list.index(cleaned_word)] = word

    # Count frequencies using a list of tuples
    word_count = []
    for word in single_word_list:
        word_count.append((word, words.count(word)))

    # Sort words by frequency (descending) and alphabetically, ignoring case
    word_count.sort(key=lambda item: item[0].lower())
    word_count.sort(key=lambda item: item[1], reverse=True)
    sorted_word_count = word_count

    # Print words with original capitalization and format
    for word, frequency in sorted_word_count:
        original_word = original_words[single_word_list.index(word)]
        print(f"{original_word}: {frequency}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        word_frequency(sys.argv[1])
    else:
        print("Error with test file, try this: python word_frequency.py <file_path>")
