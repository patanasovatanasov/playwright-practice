def clean_price(text):
    return float(text.replace('£', ''))

def stock_count(text):
    if "(" not in text:
        return 0
    text_split1 = text.split('(')
    text_split2 = text_split1[1].split(' ')
    text_strip = text_split2[0].strip()
    return int(text_strip)

def rating_to_int(word):
    dict1 = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    return dict1.get(word, 0)

def is_long_enough(password):
    return len(password) >= 8

def has_at_sign(email):
    if "@" in email:
        return True
    else:
        return False