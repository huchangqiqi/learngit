
word_filter = set()
with open('filtered_words.txt','r') as f:
    for x in f.readlines():
        word_filter |= {x.rstrip('\n')}

print(word_filter)