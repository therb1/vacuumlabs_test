import json
import re

# Constants
VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def first_consonant(splitted_word):
    for char in splitted_word:
        if char in CONSONANTS:
            return char
    raise ValueError('No consonant found')


def exaclty_one_unique_consonant(strong_consonant, splitted_word):
    for index, letter in enumerate(splitted_word):
        if letter in CONSONANTS:
            splitted_word[index] = strong_consonant

    return splitted_word


def leading_consonant(strong_consonant, splitted_word):
    if splitted_word[0] in VOWELS:
        splitted_word.insert(0, strong_consonant)
    return splitted_word


def replace_consecutive_consonants(splitted_word):
    word = ''.join(splitted_word)
    resp = re.findall(f'[{CONSONANTS}]+', word)
    resp.sort(key=len, reverse=True)
    for element in resp:
        if len(element) > 1:
            word = word.replace(element, element[0])

    return list(word)


def replace_consecutive_vowels(splitted_word):
    word = ''.join(splitted_word)
    resp = re.findall(f'[{VOWELS}]+', word)
    for element in resp:
        if len(element) > 1:
            word = word.replace(element, element[-1])

    return list(word)


def cut_all_the_consonants_after_last_vowel(splitted_word):
    if splitted_word[-1] in CONSONANTS:
        word = ''.join(splitted_word)
        resp = re.search(f'([{CONSONANTS}]*)$', word).group(1)

        return splitted_word[:-len(resp)]
    else:
        return splitted_word


def convert_to_childspeak(word):
    # Data preparation
    strong_consonant = None
    splitted_word = list(word)
    print(f"splitted_word is {splitted_word}")

    try:
        strong_consonant = first_consonant(splitted_word)
    except ValueError:
        print(f"Cant find consonant in {splitted_word}")

    # RULE №1 - Exactly one unique consonant
    r1_splitted_word = exaclty_one_unique_consonant(strong_consonant, splitted_word)

    print(f"r1_splitted_word is {r1_splitted_word}")

    # RULE №2 - Leading consonant
    r2_splitted_word = leading_consonant(strong_consonant, r1_splitted_word)

    print(f"r2_splitted_word is {r2_splitted_word}")

    # RULE №3 - No more consecutive consonants in a word
    r3_splitted_word = replace_consecutive_consonants(r2_splitted_word)

    print(f"r3_splitted_word is {r3_splitted_word}")

    # RULE №4 - No more consecutive vowels in a word
    r4_splitted_word = replace_consecutive_vowels(r3_splitted_word)

    print(f"r4_splitted_word is {r4_splitted_word}")

    # RULE №5 - ignore all the consonants after last vowel
    r5_splitted_word = cut_all_the_consonants_after_last_vowel(r4_splitted_word)

    print(f"r5_splitted_word is {r5_splitted_word}")

    return ''.join(r5_splitted_word)


if __name__ == '__main__':
    # Read data from RAW file
    with open('test materials/test.in', 'r') as file:
        data = file.read()
    data_list = data.split("\n")

    # Read data from JSON file
    f = open('test materials/test.in.json')
    data_json = json.load(f)

    childspeak_words_dict = dict()

    # Write data to output file
    with open("output/Output.txt", "w") as text_file:
        for word in data_list:
            # Create a dictionary with children's analogue of the words
            childspeak_form_of_word = convert_to_childspeak(word)

            if childspeak_form_of_word in childspeak_words_dict.keys():
                childspeak_words_dict[childspeak_form_of_word].append(word)
            else:
                childspeak_words_dict[childspeak_form_of_word] = [word]

        # Debug childspeak_words_dict
        with open("output/childspeak_words_dict.txt", "w") as text_file2:
            text_file2.write(json.dumps(childspeak_words_dict,  indent=4, sort_keys=True))

        for word in data_list:
            # Counting analogues of words
            childspeak_form_of_word = convert_to_childspeak(word)
            word_analogues = len(childspeak_words_dict.get(childspeak_form_of_word))
            text_file.write(f"{word} {word_analogues - 1}\n")
