# Bug: used > and < instead of >= and <=, so boundary years (1980, 1994) produced no output
# Fix: changed to >= and <= to include boundary years in the millennial range

year = int(input("What's your year of birth? "))

if year >= 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
