class Counter:
    def __init__(self):
        self.value = 0
    def add(self):
        self.value += 1
    def reset(self):
        self.value = 0

c = Counter()
c.add(); c.add(); c.add()
print(c.value)    # 3
c.reset()
print(c.value)    # 0