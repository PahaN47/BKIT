import random

def gen_random(begin, end, num_count):
    return [random.randint(begin, end) for i in range(num_count)]
