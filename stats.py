import sys
def word_count():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {(sys.argv[1])}")
    print("----------- Word Count ----------")
    with open(str(sys.argv[1])) as f:
        count = 0
        book = f.read()
        num_words = book.split()
        for word in num_words:
            count += 1
        print(f"Found {count} total words")

def count_char():
    
    char_count = {}
    count = 0
    with open(str(sys.argv[1])) as f:
        words = f.read()
        lower_words = words.casefold()
        for char in lower_words:
            if char.isalpha():
                if char != char.isspace(): 
                    char_count[char] = char_count.get(char,0)+1
                   
    return char_count
def sort_on(items):
    return items["num"]

def sorting(char_count):
    sorted = []
    print("--------- Character Count -------")
    for k,v in char_count.items():
        new_char = {"char" : k ,"num" : v}
        sorted.append(new_char)
    
    sorted.sort(reverse=True,key=sort_on)
    for i in range(0,len(sorted)):
        print(f"{sorted[i]["char"]}: {sorted[i]["num"]}")
    print("============= END ===============")


    
    
                  
               


                
               
   
                
        
            

