class HashMap:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def get_bucket(self, key):
        hashed_key = hash(key)%self.size
        return self.hash_table[hashed_key]

    def set_value(self, key, value):
        bucket = self.get_bucket(key)
        key_found = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                key_found = True
                break
        if key_found:
            bucket[index] = ((key, value))
        else:
            bucket.append((key, value))

    def get_value(self, key):
        bucket = self.get_bucket(key)
        key_found = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                key_found = True
                break
        if key_found:
            return record_value
        else:
            return None

    def pop(self, key, default):
        bucket = self.get_bucket(key)
        key_found = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                record = None
                key_found = True
                break
        if key_found:
            return record_value
        else:
            return default

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashMap(256)
hash_table.set_value('test@test.com', {'first_name':'test', 'last_name':'user'})
hash_table.set_value('testies@test.com', {'first_name':'noob', 'last_name':'tube'})
print("pop", hash_table.pop('testies@test.com', 'item not found'))
hash_table.set_value('testies@test.com', {'first_name':'noob', 'last_name':'tube'})
print(hash_table)
