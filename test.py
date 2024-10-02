from itertools import zip_longest

# Two simple lists representing names and favorite fruits
names = ["Alice", "Bob", "Charlie"]
fruits = ["Apple", "Banana"]

# Combine the two lists using zip_longest
for name, fruit in zip_longest(names, fruits, fillvalue="N/A"):
    # Print each pair with 20 characters wide for alignment
    print(f"{name.ljust(20)} {fruit.ljust(20)}")
