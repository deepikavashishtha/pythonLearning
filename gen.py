"""Modules for demonstrating generator execution"""

def take(count, iterable):
    """
    This method takes items from iterable 
    :param count: 
    :param iterable: 
    :return: generator
    Yields: At most 'count' items from 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


if __name__=='__main__':
    run_take()

