import sys

from stats import count_words
from stats import count_chars
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as book:
        text = book.read()
    return text

def main():  
    print("============ BOOKBOT ============")
    #print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    n_words = count_words(book_text)
    print(f"Found {n_words} total words")
    
    print("--------- Character Count -------")
    sorted = sort_chars(count_chars(book_text))    
    for dict in sorted:
        print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()
