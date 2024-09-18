def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    make_report(book_path, text)
     

def make_report(book_path, text):
    print(f"--- Begin report of{book_path} ---")
    
    word_count = get_word_count(text)
    print(f"{word_count} words found in book \n")
    
    char_dict = get_char_dict(text)
    
    list_of_chars = list(char_dict.items())
    list_of_chars.sort(reverse=True, key= sort_on)
    
    for c in list_of_chars:
        print(f"The '{c[0]}' character was found {c[1]} times")
    print(f"--- End report ---")
    pass

def sort_on(dict):
    #return second element (count) of tuple
        return dict[1]

def get_char_dict(text):
    #text.lower to lowercase all characters
    #splitting string into a list 
    num_chars = {}
    for c in text.lower():
        if c.isalpha():
            num_chars[c] = num_chars.get(c, 0) + 1
        # if c.isalpha():
        #   if c in num_chars:
        #       num_chars[c] += 1 
        #   else: 
        #       num_chars[c] = 1
    
    return num_chars

def get_word_count(text):
    words = text.split()
    # Using len() to return numbers of items in object (string)
    return len(words)
    
    # loop version
    # count = 0
    # for word in words:
    #     count += 1
    # return count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()


