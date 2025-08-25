def count_words(file_contents):
    words = file_contents.split()
    #print(f"{len(words)} words found in the document")
    return(f"{len(words)}")

def count_letters(file_contents):
    file_contents = file_contents.lower()
    letters_count = {}
    for i in file_contents:
        if i in letters_count:
            letters_count[i] += 1
        else:
            letters_count[i] = 1
            #print(letters_count)
    return(letters_count)

def sort_dict2(sorted_letters):
    for i in sorted_letters:
        value1 = sorted_letters.get(i)
        value2 = i
        sorted = ["char:", value2, "num:", value1]
        print(sorted)

def sort_dict(sorted_letters):
    sorted_items = sorted(sorted_letters.items(), reverse=True, key=lambda x: x[1])
    output = []
    for key, value in sorted_items:
        if key.isalpha():
            output.append(["char:", key, "num:", value])
    return(output)