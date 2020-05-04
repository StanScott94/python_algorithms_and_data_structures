from collections import Counter

buckets = [ ('john.doe@example.com',{'first_name':'john','last_name':'doe'}),
            ('jane.doe@example.com',{'first_name':'jane','last_name':'doe'}),
            ('derek.zoo@example.com',{'first_name':'derek','last_name':'zoolander'}),
            ('murph.cooper@example.com',{'first_name':'murph','last_name':'cooper'}),
            ('ned.stark@example.com',{'first_name':'ned','last_name':'stark'})
            ]

def get_last_name_count(list_of_records):
    """
    fill in docstring
    """
    list_of_last_names = []
    for item in list_of_records:
        email, full_name = item
        list_of_last_names.append(full_name['last_name'])
    return Counter(list_of_last_names)

def compare_full_name(list_of_records, email, first_name, last_name):
    """
    fill in docstring
    """
    for item in list_of_records:
        record_email, full_name = item
        if email == record_email:
            return first_name == full_name['first_name'] and last_name == full_name['last_name']
    return False

def update_record(list_of_records, email, first_name, last_name):
    """
    fill in docstring
    """
    found_email = False
    for index, record in enumerate(list_of_records):
        record_email, full_name = record
        if record_email == email:
            found_email = True
            break
    if found_email:
        list_of_records[index] = (email, {'first_name':first_name, 'last_name':last_name})
    else:
        list_of_records.append((email, {'first_name':first_name, 'last_name':last_name}))

def divider():
    print()
    print("-"*40)
    print()

print("The last names and their counts are as follows:")
result = get_last_name_count(buckets)
for k, v in result.items():
    print(f"{k}: {v}")
divider()

print("Does ned's first and last name match our records?")
print(compare_full_name(buckets,'ned.stark@example.com','ned','stark'))
divider()

print("Changing john's first name to jon and last name to snow")
update_record(buckets,'john.doe@example.com','jon','snow')
divider()

print("Adding new record ironman@example.com")
update_record(buckets,'ironman@example.com','iron','man')
divider()

print("Updated last names and their count are as follows:")
result = get_last_name_count(buckets)
for k, v in result.items():
    print(f"{k}: {v}")
divider()

print("Full list")
for item in buckets:
    record_email, full_name = item
    print(f"Email: {record_email}, first name: {full_name['first_name']}, last_name: {full_name['last_name']}")
