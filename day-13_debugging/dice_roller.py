# bug: incorrect randint range used (1, 6), resulted in IndexError.
#fix: fixed randint range to (0, 5)


from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
