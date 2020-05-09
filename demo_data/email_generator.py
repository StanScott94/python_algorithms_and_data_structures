from random import randint, choice
from string import ascii_lowercase as letters

def generate_name(length_of_name):
        return ''.join(choice(letters) for index in range(length_of_name))

def email_generator(list_size, emails_to_add=[], length_of_name=10, list_of_domains=None):

    if list_of_domains is None:
        list_of_domains = ["@python.com", "@java.co.uk", "@cobol.net", "@assembler.co.za"]

    list_of_emails = []
    for index in range(list_size):
        list_of_emails.append(generate_name(length_of_name) + choice(list_of_domains))

    for email in emails_to_add:
        list_of_emails.append(email)

    return sorted(list_of_emails)
