with open('input.txt', 'r') as f:
    lines: list[str] = f.readlines()
    lines_count: int = len(lines)
    words: list[str] = ' '.join(lines).split()
    words_count: int = len(words)
    letters_count: int = sum([len(i.replace('.', "")) for i in words])

    print(f"Input file contains:\n {letters_count} letters\n {words_count} words\n {lines_count} lines")
