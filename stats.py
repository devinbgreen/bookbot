def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_chars(text):
    letter_count_dictionary = {}
    for char in text:
        letter_count_dictionary[char.lower()] = letter_count_dictionary.get(char.lower(), 0) + 1
    return letter_count_dictionary

def sort_on(items):
    return items["num"]

def sort_chars(letters):
    char_dicts = []
    for letter, amount in letters.items():
        if letter.isalpha():
            new_dict = {"char": letter, "num": amount}
            #print(new_dict)
            char_dicts.append(new_dict)
                
    char_dicts.sort(reverse=True, key=sort_on)
    #print(char_dicts)
    return char_dicts