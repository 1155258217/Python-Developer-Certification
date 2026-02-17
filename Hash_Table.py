class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {key: value}
        else: 
            self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection.keys():
            if isinstance(self.collection[hashed_key], dict):
                del self.collection[hashed_key][key]
            else:
                del self.collection[hashed_key]
    
    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            return self.collection[hashed_key][key]
        return None


