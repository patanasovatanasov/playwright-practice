def clean_price(text):
    return float(text.replace('£', ''))

print(clean_price("£51.77") * 2)    # трябва да изведе 103.54