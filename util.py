import os
import random

# Function to get random from file
def get_random_from_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r+') as r:
            things = r.readlines()
            thing = random.choice(things).strip()
            return thing
    else:
        print(f"{file_path} does not exist!")