""" practise with generators: create iterables with functions
These sequences are evaluated lazily (only compute the next element on demand)
Generators contain at least an yield statement; might contain return with no arguments;
There's an implicit return at the end of the definition
Generators are good for modelling infinite or very large sequences (e.g. sensor readings, math sequences, content of
large files
Generators are single use objects. Each time we call a generator function we create a generator object.
To recreate a generator from a generator expression you must execute the expression again.
"""


def take(count, iterable):
    """
    retrieves a specified number of elements from the front of an iterable
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return  # the sequence of elements ends when the previous condition is met
        counter += 1
        yield item


def distinct(iterable):
    """
    eliminates duplicate items using a set
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue  # finish current loop iteration and begin the next iteration immediately
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


if __name__ == '__main__':
    run_pipeline()
