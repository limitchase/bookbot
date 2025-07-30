import sys
from stats import get_num_words, get_char_count, get_pretty_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_path = sys.argv[1]
    
    # text_path = "./books/frankenstein.txt"
    # print(get_book_text(text_path))
    # print(f"{get_num_words(text_path)} words found in the document")
    word_count = get_num_words(text_path)
    char_count = get_char_count(text_path)
    # print(char_count)
    sorted_dict = get_pretty_dict(text_path)

    book_report = f"""
============ BOOKBOT ============
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
    """
    print(book_report)
    for c, c_count in sorted_dict:
        if c.isalpha():
            print(f"{c}: {c_count}")
    print("============= END ===============")
main()