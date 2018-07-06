# Create a tuple named `zoo` that contains your favorite animals.
my_zoo = ('lion', 'tiger', 'bear', 'gerbil')

# Find one of your animals using the `.index(value)` method on the tuple.
index = my_zoo.index('tiger')
print(index)

# Determine if an animal is in your tuple by using `for value in tuple`.
for animal in my_zoo:
    if animal == "owl":
        print("hootie hoooo")
    else:
        print("not an owl")

# Create a variable for each of the animals in your tuple with this cool feature of Python. (destructuring, aka, unpacking)

    # ```
    # # example
    # (lizard, fox, mammoth) = zoo
    # print(lizard)
    # ```
(big_cat, striped_cat, grumpy_lump, little_thing) = my_zoo
print(striped_cat)

# Convert your tuple into a list.
zoo_List = list(my_zoo)
print(zoo_List)

# Use `extend()` to add three more animals to your zoo.
zoo2 = ['owl', 'python', 'wolf']
zoo_List.extend(zoo2)
print(zoo_List)

# Convert the list back into a tuple.
my_zoo = tuple(zoo_List)
print(my_zoo)