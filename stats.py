def count_words(book_text):
    number_of_words = book_text.split()
    return len(number_of_words)

def count_chars(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
          char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(items):
    return items["count"]

def sort_chars(char_dict):
    char_list = [{"char" : key, "count" : value} for key, value in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list