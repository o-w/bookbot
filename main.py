def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    from stats import count_words, count_letters, sort_dict
    import sys
    file_to_read = ""

    if sys.argv[1:]:
        file_to_read = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        #file_to_read = "books/frankenstein.txt"A

    all_words = get_book_text(file_to_read)
    word_count_string = count_words(all_words)
    letter_count_dict = count_letters(all_words)
    new_sorted_dict = sort_dict(letter_count_dict)

    # print results

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + file_to_read + "...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_string} total words")
    print("--------- Character Count -------")
    for char, charval, num, numval in new_sorted_dict:
        print(f"{charval}: {numval}")

    print("============= END ===============")

    #print(word_count_string)
    #print(letter_count_dict)
main()