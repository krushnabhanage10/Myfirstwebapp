import operator

def froml(article):
    words = article.split()
    word_count = len(words)
    dict = {}

    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    var_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    return word_count,var_dict