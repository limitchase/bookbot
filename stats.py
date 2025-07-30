def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    word_count = len(get_book_text(text).split())
    return word_count

def get_char_count(text):
    char_count = dict()
    split_text = list(get_book_text(text))
    for c in split_text:
        char_count[c.lower()] = char_count.get(c.lower(), 0) + 1
    return char_count

def get_pretty_dict(text):
    char_dict = get_char_count(text)
    sorted_dict = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_dict