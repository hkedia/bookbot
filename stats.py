def get_num_words(file_content):
    return len(file_content.split())

def get_num_chars(file_content):
    char_count = {}
    for char in file_content:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sorted_dictionary(dict_of_chars):
    characters = []
    for item in dict_of_chars:
        characters.append({"char": item, "num": dict_of_chars[item]})
    characters.sort(reverse=True, key=sort_on)
    return characters
    
