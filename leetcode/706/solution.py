# copy 705
class MyHashMap:

    def __init__(self):
        self.count = 0
        self.max = 16
        self.array = [[] * _ for _ in range(self.max)]

    def put(self, key: int, value: int) -> None:
         if self.count > (0.75 * self.max):
            self.max *= 2
            new_array = [[] * _ for _ in range(self.max)]
            for i in range(len(self.array)):
                if len(self.array[i]) > 0:
                    for j in range(len(self.array[i])):
                        val = self.hashcode(self.array[i][j][0])
                        index = val % self.max
                        new_array[index].append(self.array[i][j])
            self.array = new_array
         self.remove(key)
         self.array[self.hashcode(key) % self.max].append((key, value))
         self.count += 1

    def get(self, key: int) -> int:
        val = self.hashcode(key)
        index = val % self.max
        n = len(self.array[index])
        for i in range(n):
            if self.array[index][i][0] == key:
                return self.array[index][i][1]
        return -1

    def remove(self, key: int) -> None:
        val = self.hashcode(key)
        index = val % self.max
        n = len(self.array[index])
        for i in range(n):
            if self.array[index][i][0] == key:
                self.array[index].pop(i)
                self.count -= 1
                return

    def hashcode(self,key):
        code = key
        if code < 0:
            code *= -1
        return code//37+1

obj = MyHashMap()
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.get(3))
print(obj.put(2, 1))
print(obj.get(2))
print(obj.remove(2))
print(obj.get(2))
