def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    

    wCount = wordCount(file_contents)
    cCount = charCount(file_contents)
    reportPrint(wCount, cCount, path_to_file)

def wordCount(book):
    return len(book.split())

def charCount(book):
    words = book.split()
    letters = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    
    return letters

def reportPrint(words, chars, path):
    print(f"---Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    
    sortedChars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sortedChars:
        if char.isalpha():
            if count != 1:
                print(f"The '{char}' character was found {count} times")
            else:
                print(f"The '{char}' character was found {count} time")
    print("--- End report ---")
        
    

if __name__ == "__main__":
    main()