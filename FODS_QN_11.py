import string

with open('sample_text.txt', 'r') as file:
    data = file.read()

words = data.split()

translator = str.maketrans('', '', string.punctuation)
words = [word.translate(translator).lower() for word in words]

word_freq = {}
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

for word, freq in sorted_word_freq:
    print(f"{word}: {freq}")
