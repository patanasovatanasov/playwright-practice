def rating_to_int(word):
    dict1 = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    return dict1.get(word, 0)
print(rating_to_int('Three'))