def search_word_in_file(word, file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        word_lower = word.lower()
        text_lower = text.lower()
        count = text_lower.count(word_lower)
        return count

def main():
    file_name = 'input.txt'
    word_to_find = input("Введите слово для поиска в файле: ")
    count = search_word_in_file(word_to_find, file_name)
    print(f"Слово '{word_to_find}' найдено {count} раз(а) в файле {file_name}")

if __name__ == "__main__":
    main()
