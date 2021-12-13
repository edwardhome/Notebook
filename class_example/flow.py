import time
from argparse import ArgumentParser

def flow(n="break"):
    i = 0
    if n == "break":
        while True:
            if i > 9:
                break
            else:
                print(i)
                time.sleep(0.5)
                i += 1
    elif n == "contiune":
        for i in range(10):
            if i % 2 == 0:
                continue
            else:
                i += 1
            print(i)
            time.sleep(0.5)
    elif n == "pass":
        for i in range(10):
            if i == 5:
                pass
            else:
                time.sleep(0.5)
                print(i)
            i += 1
            

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("type", help="選擇內容 break or contiune or pass", type=str)
    args = parser.parse_args()
    flow(args.type)