from stats import get_num_words, get_num_characters, sort
import sys 

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def print_report(filePath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print("Found {} total words".format(get_num_words(get_book_text(filePath))))
    print("--------- Character Count -------")
    characters = get_num_characters(get_book_text(filePath))
    characters = sort(characters)
    for item in characters:
        character = item["char"]
        if character.isalpha():
            print(f"{character}: {item['num']}")
    print("============= END ===============")


def main():
    if not(len(sys.argv) == 2): 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filePath = sys.argv[1]
    print_report(filePath)


main()