import time
from demo_data.record_generator import record_generator
from demo_data.email_generator import email_generator
from data_types.hash_map import HashMap

def generate_record_file(total_records, path):
    with open(path, "w") as writer:
        for index in range(total_records):
            key = email_generator()
            value = record_generator()
            writer.write(key[0] + ":" + value + "\n")
        writer.write("you_found_me@nice.com:jonathan,brites,full stack developer\n")
        writer.write("another_one_to_find@nice.com:andreas,raede,noob developer\n")

def populate_hashmap_from_file(path, hashmap):
    with open(path, "r") as reader:
        for record in reader:
            key, value = record.split(":")
            hashmap.set_value(key, value)

def hashmap_analyzer():
    path = "test_records.txt"
    size_records_list = 150000
    generate_record_file(size_records_list, path)
    hashmap = HashMap(256)
    populate_hashmap_from_file(path, hashmap)
    records_found = []
    start_time = time.time()
    records_found.append(hashmap.get_value("you_found_me@nice.com"))
    records_found.append(hashmap.get_value("another_one_to_find@nice.com"))
    execution_time = time.time() - start_time
    print(f"{HashMap.__name__.capitalize()} -> found {len(records_found)} records in a list of {size_records_list}, Time Elapsed : {execution_time:.5f}")

hashmap_analyzer()
