## 7. Counter — Track Count

class Counter:
    def __init__(self):
        self.count = 0   # shuru me count = 0

    def increment(self):
        self.count += 1  # matlab: self.count = self.count + 1

    def display(self):
        print("Count:", self.count)

c = Counter()
c.increment() # 0 + 1 = 1
c.increment() # 1 + 1 = 2
c.display()


