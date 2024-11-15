from sample_madlibs import test1, test2, test3
import random

if __name__ == "__main__":
    m = random.choice([test1, test2, test3])
    m.madlib()