class StrIntMap:

    def __init__(self):
        self.capacity = 8
        self.count = 0
        self.table = [[] for i in range(self.capacity)]

    def _hash(self, key: str):
        return abs(hash(key)) % self.capacity

    def put(self, key: str, value: int) -> None:
        index = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1
        if self.count / self.capacity > 0.75:
            self.rehash()

    def get(self, key: str):
        index = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key: str):
        index = self._hash(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.count -= 1
                return

    def contains(self, key: str):
        return self.get(key) is not None

    def size(self):
        return self.count

    def keys(self):
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(pair[0])
        return result

    def rehash(self) -> None:
        old_table = self.table
        self.capacity = self.capacity * 2
        self.table = [[] for _ in range(self.capacity)]
        self.count = 0
        for bucket in old_table:
            for pair in bucket:
                self.put(pair[0], pair[1])
