import nltk as nk

reviews = open('ice_cream_reviews.txt')
'''
for review in reviews:
    print('\n')
    #print(review)
    tokens = nk.word_tokenize(review)
    #print(tokens)
    pos_tags = nk.pos_tag(tokens)
    #print(pos_tags)
    for tag in pos_tags:
        if tag[1] == 'JJ' or tag[1] == 'JJR' or tag[1] == 'JJS':
            print(tag)
'''
        if tag[0] not in stop_words:
            new.text.append(tag[0])
    print('\n')
    print
    print
    print
