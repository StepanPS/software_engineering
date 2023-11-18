import re


def count_words(filename: str) -> tuple[int, str]:
    with open(filename, 'r', encoding='utf-8') as file:
        words: list[str] = [i for i in [re.sub("[-!.:«»,?""]", '', w.lower()) for w in file.read().split()] if
                            not i == ""]
        words_count: int = len(words)
        d: tuple[str, int] = sorted([(i, words.count(i)) for i in set(words)], key=lambda t: t[1], reverse=True)[0]
        return words_count, d[0]


count, word = count_words("Book.txt")
print(f"Кол-во слов: {count}\n Самое частое слово:'{word}'")
