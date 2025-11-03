import sys
from stats import word_count
from stats import count_char
from stats import sorting

def get_book_text():
    with open(sys.argv) as f:
        file_contents = f.read()
        return file_contents 
    

def main():
    if len(sys.argv) != 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    
    word_count()
    sorting(count_char())
    



main()