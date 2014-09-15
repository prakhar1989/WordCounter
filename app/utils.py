from collections import Counter
import random

### HELPERS ###
def validate_word_count(text, words_excluded, words_returned):
    cnt = Counter()
    ignore_words = words_excluded.split()
    for word in text.split():
        if word not in ignore_words:
            cnt[word] += 1
    for word in cnt:
        if  words_returned.get(word) and \
                str(cnt[word]) != words_returned[word]:
            return False
    return True

def generate_token():
    return random.randrange(100000, 999999)

def get_random_text():
    text = "the quick brown fox jumped on the lazy dog"
    return text, ["quick", "brown", "lazy"]
