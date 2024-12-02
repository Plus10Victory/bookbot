def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text) 
    char_list = convert_to_list(character_count)   

    print(f"--- Begin report of {book_path} ---")    
    print(f"{num_words} words found in the document")
    print("")
    print_charcter_count(char_list)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

# takes whole text, lowers character, checks if character is alpha, updates dict, & returns dict
def get_character_count(text):
    character_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered not in character_dict:
                character_dict[lowered] = 1
            else:
                character_dict[lowered] += 1
    return character_dict 

# convert dict to list of dict
def convert_to_list(char_dict):
    char_list = []
    for i in char_dict:
        char_list.append({"char": i, "num": char_dict[i]})
    return char_list

# defines sorting
def sort_on(dict):
    return dict["num"]

# takes list of dicts, loops through, and prints the values of each key pair from dict
def print_charcter_count(char_list):
    char_list.sort(reverse=True, key=sort_on)
    for i in char_list:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    return

main()