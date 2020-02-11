import random

SEPERATOR = set([" ", "，", "。", ",", ";", ",", "?", ".", "？", "；"] \
    + ["“", "”", "#","、", "【", "】", "《", "》", "[", "]", '"', "'"] \
    + ["-", "-", "_", "\n", "\t"])

def is_ascii(c):
    return ord(c) < 128
    
def is_seperator(c):
    return c in SEPERATOR
    
def tokenize(src_txt):
    token_list = []
    token = ""
    for c in src_txt:
        if is_ascii(c):
            token += c
        else:
            if token != "":
                token_list.append(token)
                token = ""
            token_list.append(c)
    if token != "":
        token_list.append(token)
    return token_list

def reorder(token_list):
    n_grams = [2, 3]
    i = 0
    if len(token_list) <= 3:
        return token_list

    token_list_reordered = [token_list[0]]
    middle_token_list = token_list[1:-1]

    while (i<len(middle_token_list)):
        n_gram = random.choice(n_grams)
        j = min(i+n_gram, len(middle_token_list))
        n_gram = middle_token_list[i:j]
        random.shuffle(n_gram)
        token_list_reordered.extend(n_gram)
        i = j

    token_list_reordered.append(token_list[-1])

    return token_list_reordered
    
def sentencize(src_txt):
    sentence = ""
    reordered_txt = []
    for c in src_txt:        
        if is_seperator(c):
            reordered_txt.extend(reorder(tokenize(sentence)))
            reordered_txt.append(c)
            sentence = ""
        else:
            sentence += c
    if sentence != "":
        reordered_txt.extend(reorder(tokenize(sentence)))
    return "".join(reordered_txt)
