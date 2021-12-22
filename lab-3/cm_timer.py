import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.begin = time.time()
    
    def __exit__(self, type, value, traceback):
        print("time:", time.time() - self.begin)

@contextmanager
def cm_timer_2():
    begin = time.time()
    yield
    print("time:", time.time() - begin)

if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(4.7)

    with cm_timer_2():
        time.sleep(4.7)
    