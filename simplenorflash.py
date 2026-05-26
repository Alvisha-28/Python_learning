import numpy as np

class NorFlash:
    def __init__(self):
        # Create a 4 x 4 x 64 x 64 array
        self.data = np.random.randint(0, 2, size=(4, 4, 64, 64), dtype=np.uint8)

    def read(self, a, b, c, d, e):
        return self.data[a, b, c, d:e]

    def write(self, a, b, c, d, values):
        for i in range(len(values)):
            self.data[a, b, c, d + i] = values[i]


store = NorFlash()

print(store.read(2, 2, 12, 8, 16))

values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
store.write(2, 2, 12, 8, values)

print(store.read(2, 2, 12, 8, 8+len(values)))