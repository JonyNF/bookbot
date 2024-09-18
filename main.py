def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    # print(f"{word_count} words found in book")
    
    char_count = get_char_count(text)
    # print(f"{char_count} characters found in book")    
    
def get_char_count(text):
    #text.lower to lowercase all characters
    #splitting string into a list 
    characters = [c for c in text.lower()]
    num_chars = {}
    for c in characters:
        if c in num_chars:
            num_chars[c] += 1 
        else: 
            num_chars[c] = 1
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


