sentence = input("Введите предложение на английском: ")
print("Длина предложения:", len(sentence))

lowercase_sentence = sentence.lower()
print("Предложение в нижнем регистре:", lowercase_sentence)

vowels_count = {}
vowels = ['a', 'e', 'i', 'o', 'u']
for char in lowercase_sentence:
    if char in vowels:
        if char not in vowels_count:
            vowels_count[char] = 1
        else:
            vowels_count[char] += 1
for vowel, count in vowels_count.items():
    print(f"Буква '{vowel}' встречается: {count} раз(a)")

modified_sentence = lowercase_sentence.replace("ugly", "beauty")
print("Заменa 'ugly' на 'beauty':", modified_sentence)

The_end = ['the', 'end']
for i in The_end:
    if i in sentence:
        print('Предложение начинается с "The" и заканчивается на "end"')
        break
else:
    print('Предложение не начинается с "The" и не заканчивается "end"')
