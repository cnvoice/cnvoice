import random
def is_ascii(c):
    return ord(c) < 128
    
def is_seperator(c):
    return c in [" ", "，", "。", ",", ";", ",", "?", ".", "？", "；"] \
    + ["“", "”", "#","、", "【", "】", "《", "》", "[", "]", '"', "'"] \
    + ["-", "-", "_", "\n"]
    
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
    token_list_reordered = []
    while (i<len(token_list)):
        n_gram = random.choice(n_grams)
        j = min(i+n_gram, len(token_list))
        n_gram = token_list[i:j]
        random.shuffle(n_gram)
        token_list_reordered.extend(n_gram)
        i = j
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
