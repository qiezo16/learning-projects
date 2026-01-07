class HashMap:
    def __init__(self, array_size):
        self.array_size
        self.array = [None for item in range(array_size) ]
    
    def hash(self, key):
        self.key = key
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

