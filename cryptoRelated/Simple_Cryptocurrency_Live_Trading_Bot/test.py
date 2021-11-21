import sys
import time

if __name__=="__main__":
    for arg in sys.argv:
        time.sleep(5)
        print(arg)
    time.sleep(5)