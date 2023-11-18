import re

forbidden_words: list[str] = []
with open("input_1.txt", "r") as f:
    forbidden_words.extend(f.read().split())

msg: str = input("Ведите предложение или нажмите Enter для предложения по умолчанию: ")

if msg.isspace() or msg == "":
    msg = "Hello, world! Python IS the programming language of thE future. My EMAIL is… \nPYTHON is awesone!!!"

for w in forbidden_words:
    msg = re.sub(w, "*" * len(w), msg, flags=re.IGNORECASE)
print(msg)
