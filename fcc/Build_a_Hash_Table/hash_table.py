class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, string: str):
        res = []
        for s in string:
            res.append(ord(s))
        return sum(res)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {key: value}
        else:
            self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        return None
