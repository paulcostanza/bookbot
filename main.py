def word_count(book):

    words = book.split()
    total = 0

    for word in words:
        total += 1

    return total

def letter_count(book):
    letters = {}

    book = book.lower()

    for letter in book:
        letters[letter] = 1 + letters.get(letter, 0)

    return letters

def sort_letters(letter_list):
    return letter_list["num"]

def print_a_report(book, name_of_book):

    # gather data
    total_words = word_count(book)
    total_letters = letter_count(book)

    # turn object into list
    total_letters_list = []
    for letter in total_letters:
        if letter in 'qwertyuiopasdfghjklzxcvbnm':
            total_letters_list.append({"letter": letter, "num": total_letters[letter]})

    total_letters_list.sort(reverse=True, key=sort_letters)

    # display data
    print(f"--- Begin report of {name_of_book} ---")
    print(f"{total_words} words found in the document")
    print()
    
    for idx in range(len(total_letters_list)):
        print(f"The '{total_letters_list[idx]["letter"]}' character was found {total_letters_list[idx]["num"]} times")

    print("--- End report ---")

def main():

    frank = "books/frankenstein.txt"

    with open(frank) as f:
        file_contents = f.read()

    print_a_report(file_contents, frank)

main()