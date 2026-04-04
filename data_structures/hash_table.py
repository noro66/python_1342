class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


def item_in_common(list1, list2):
        items = set(list1)

        for item  in list2:
            if item in items:
                return True
        return False


def find_duplicates(nums: list):
    dups = {}
    res = []
    for num in nums:
        if num in dups:
            if dups[num] is False:
                res.append(num)
            dups[num] = True
        else:
            dups[num] = False
    return res


def first_non_repeating_char(string):
    repeated = {}
    for c in string:
        if c in repeated:
            repeated[c] = True
        else:
            repeated[c] = False
    for k, v in repeated.items():
        if v is False:
            return k
    return None
