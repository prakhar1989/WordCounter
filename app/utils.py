from collections import Counter
from faker import Factory
import random

### HELPERS ###
def validate_word_count(text, words_excluded, words_returned):
    cnt = Counter()
    ignore_words = words_excluded.split()
    for word in text.split():
        if word not in ignore_words:
            cnt[word] += 1
    for word in cnt:
        if  not words_returned.get(word) or \
                str(cnt[word]) != words_returned[word]:
            return False
    return True

# generate a random 6 digit client token
def generate_token():
    return random.randrange(100000, 999999)

def get_exclusion_words(text):
    words = text.split()
    # max number of words should be at least one but not all
    max_count = random.randrange(1, len(words)-2)
    return set(words[i] for i in random.sample(range(0, len(words)), max_count))

def generate_random_text():
    fake = Factory.create()
    text = fake.text()
    words = " ".join(get_exclusion_words(text))
    return text, words
