Sentence = "Penculikan,Pemerkosaan,Pembunuhan"
words = Sentence.split(",")
print(words)

def clean_word(word):
    return word.strip()

cleaned_words = list(map(clean_word, words))
print(cleaned_words)

print(",".join(cleaned_words))