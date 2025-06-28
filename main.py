import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as book:
        file_contents = book.read()
    return file_contents

def main():
    #book_path = "./books/frankenstein.txt"
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    count_of_words = count_words(book_text)
    count_of_chars = count_chars(book_text)
    ordered_char_list = sort_chars(count_of_chars)
    print_report(book_path, count_of_words, ordered_char_list)

def print_report(book_path, count_of_words, ordered_char_list):   
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {count_of_words} total words
--------- Character Count -------""")
    for char in ordered_char_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()