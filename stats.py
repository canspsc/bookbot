def count_words (book_text):
    words = book_text.split()
    return len(words)

def get_num_characters(book_text):
    characters = {}
    for character in book_text:
        character = character.lower()
        if character in characters:
            characters[character] += 1
        else: 
            characters[character] = 1
    return characters
    

