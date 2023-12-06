class FileEmptyException(Exception):
    def __init__(self, filename: str):
        message: str = f"Файл {filename} пустой"
        super().__init__(message)


def open_file(filename: str) -> str:
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        if content.strip() == '':
            raise FileEmptyException(filename)
        return content


def main(filename: str) -> None:
    try:
        print(open_file(filename))
    except FileEmptyException as ex:
        print(ex)


if __name__ == '__main__':
    main("No text.txt")
    main("Text.txt")
