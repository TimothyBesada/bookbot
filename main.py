from typing import Dict, List

def main() -> None:
    book_path = "books/frankenstein.txt"
    print(create_report(book_path))


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def get_word_count(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> Dict[str, int]:
    cleaned_text = ''.join(char for char in text if char.isalpha())
    char_count = {}
    for char in cleaned_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return sort_char_dict(char_count)

def sort_char_dict(char_dict: Dict[str, int]) -> List[Dict[str, int]]:
    list_chars = [item for item in char_dict.items()]
    return sorted(list_chars, key=lambda x: x[1], reverse=True)

def create_report(path: str) -> str:
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)

    report = f"--- Begin report of {path} ---\n"
    report += f"{word_count} words found in the document\n\n"
    for char, count in char_count:
        report += f"The '{char}' character was found {count} times\n"
    report += "--- End of report ---"
    
    return report

main()