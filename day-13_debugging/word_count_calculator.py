#bug: used == for word_per_page which contradicted the earlier declaration.
#fix: replaced == with = that fixed the code

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
