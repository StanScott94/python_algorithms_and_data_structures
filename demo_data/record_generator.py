from random import choice

def record_generator():
    first_names = ["julie", "john", "jack", "mary", "hans", "gene", "sahra", "max", "abby"]
    last_names = ["smith", "johnson", "peters", "maxwel", "tohmson", "james", "hansmann"]
    roles = ["scrum master", "backend developer", "frontend developer", "project manager", "product owner"]

    return ''.join(choice(first_names) + "," + choice(last_names) + "," + choice(roles))
