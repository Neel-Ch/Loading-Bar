import time

class LoadingBar:
    def __init__(self, load_size, load_per_sec):
        self.size = load_size
        self.speed = load_per_sec

    def load(self):
        blocks = int(self.size/self.speed)
        bar = ""
        for block in range(blocks):
            bar += "⬛"
        print(bar, end="\r")
        for i in range(blocks):
            time.sleep(1)
            print("⬜" * i, end="")
            print(bar[i:], end="")
            print(f" ({i*self.speed}/{self.size})", end="\r")
        time.sleep(1)
        print("⬜" * blocks, end="")
        print(f" ({self.size}/{self.size}) Done!")

def __main__():
    bar = LoadingBar(100, 1)
    bar.load()

__main__()
