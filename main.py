def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(path):
    letters = {}
    with open(path) as f:
        file_contents = f.read()
    for char in file_contents:
        if char.isalpha():
            char = char.lower()
            letters[char] = letters.get(char, 0) + 1
    return letters


def report(path):
    letters = count_letters(path)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(path)} words found in the document")
    for letter, count in sorted(
        letters.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")


report("books/frankenstein.txt")
