class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = 10 # hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value) #update existing
        else:
            bucket.append((key, value)) # add new

    def get_val(self, key):
        hashed_key = 10 # hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found"

    def delete_record(self, key):
        hashed_key = 10 # hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.remove((record))
        else:
            return "No record found"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
hash_table.set_val('chris@example.com','some value')
hash_table.set_val('notchris@example.com','some other value')
print(hash_table)
#hash_table.set_val('chris@example.com', 'I love Python')
#python3 hash_algo.pyprint(hash_table)
#print(hash_table.get_val('chris@example.com'))
#print(hash_table.get_val('somebody@example.com'))
hash_table.delete_record('chris@example.com')
print(hash_table)
