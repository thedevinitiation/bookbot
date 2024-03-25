
def get_book_content(path):
    with open(path) as f:
        return f.read()


def get_book_num_words(content):
    return len(content.split())


def get_num_char(text):
    result = {}
    for c in text:
        if result.get(c) is None:
            result[c] = 1
        else:
            result[c] += 1
    return result


def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_content(path_to_book).lower()
    num_words = get_book_num_words(text)
    num_char = get_num_char(text)

    # Create report
    header = f"--- Begin report of {path_to_book} ---\n{num_words} words found in the document\n"
    print(header)
    sorted_num_char = dict(sorted(num_char.items(), key=lambda item: item[1], reverse=True))
    for k, v in sorted_num_char.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")


main()