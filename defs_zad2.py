def stock_count(text):
    if "(" not in text:
        return 0
    text_split1 = text.split('(')
    text_split2 = text_split1[1].split(' ')
    text_strip = text_split2[0].strip()
    return int(text_strip)
print(stock_count("In stock (22 available)"))