list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
number = [int(num) for num in list_of_strings]
even_numbers = [num for num in number if num%2 == 0]
print(even_numbers)
