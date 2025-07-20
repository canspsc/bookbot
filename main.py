from stats import get_num_words, get_num_characters, sort

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found {} total words".format(get_num_words(get_book_text("books/frankenstein.txt"))))
    print("--------- Character Count -------")
    characters = get_num_characters(get_book_text("books/frankenstein.txt"))
    characters = sort(characters)
    for item in characters:
        character = item["char"]
        if character.isalpha():
            print(f"{character}: {item['num']}")
    print("============= END ===============")

main()

