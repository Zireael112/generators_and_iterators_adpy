from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# Iterator
class FlatIterator(list):
    def __iter__(self):
        self.value = iter(value for value in nested_list)
        return self

    def __next__(self):
        next_value = next(self.value)
        if not isinstance(next_value, list):
            return next_value
        self.value = chain(self.value, next_value)
        return next(self)


# Iteration
for item in FlatIterator(nested_list):
    print(item)

# List comprehension
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# Function with generation
def flat_generator(list_):
    copy_list = len(list_)
    while copy_list != 0:
        for items in list_:
            for item in items:
                yield item
            copy_list -= 1


for item in flat_generator(nested_list):
    print(item)