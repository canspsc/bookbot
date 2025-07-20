def get_num_words(book_text):
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

def sort_key(item):
    return item["num"]
    
def sort(characters):
    result_list = []

    for char, count in characters.items():
        item = {"char": char, "num": count}
        result_list.append(item)

    result_list.sort(key=sort_key)
    return result_list
    
