import sys
from stats import number_words
from stats import character_count
from stats import sort_dictionary

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookname = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookname}...")
    contents = get_book_text(bookname)
    num_words = number_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    character_counts = character_count(contents)
    sorted_character_counts = sort_dictionary(character_counts)
    print("--------- Character Count -------")
    for counted_character in sorted_character_counts:
        print(f"{counted_character['character']}: {counted_character['count']}")
    print("============= END ===============")

main()