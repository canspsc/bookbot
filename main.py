from stats import count_words, get_num_characters

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def main ():
    print("{} words found in the document".format(count_words(get_book_text("books/frankenstein.txt"))))
    characters = get_num_characters(get_book_text("books/frankenstein.txt"))
    print(characters)

main()

