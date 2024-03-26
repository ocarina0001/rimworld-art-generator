import root
import util
import random
import re
import os

# Variables
curly = r'\{([^}]+)\}'

def main():
    # Globals
    global curly
    
    # Pull a random description from root
    art = random.choice(root.AllArt)
    description = random.choice(art)
    
    failure_count = 0
    # Begin the LOOP
    while failure_count <= 100:
        # Check for any {}
        matches = re.findall(curly, description)
        #print(matches)
        # Exit loop if no more matches are found
        if len(matches) <= 0:
            break
        # For each match...
        for match in matches:
            try:
                if hasattr(root, match):
                    #print(f"{match} exists in root!")
                    attribute = getattr(root, match)
                    # Check if it's a list
                    if isinstance(attribute, list):
                        #print(f"{match} is a list!")
                        choice = random.choice(attribute)
                        #print(f"{match} became {choice}!")
                        description = description.replace("{" + match + "}", choice, 1)
                    # Check if it's a function
                    elif callable(attribute):
                        #print(f"{match} is a function!")
                        result = attribute()
                        #print(f"{match} became {result}!")
                        description = description.replace("{" + match + "}", result, 1)
                    else:
                        #print(f"{match} exists, but it's not list nor function nor file.")
                        failure_count += 1
                # Check if it's a file
                elif os.path.exists(f"Words/{match}.txt"):
                    #print(f"{match} is a file!")
                    choice = util.get_random_from_file(f"Words/{match}.txt")
                    #print(f"{match} became {choice}!")
                    description = description.replace("{" + match + "}", choice, 1)
                # Attempt a special check
                elif not hasattr(root, match):
                    special = root.special(match)
                    if special != False:
                        #print(f"{match} is special!")
                        description = description.replace("{" + match + "}", special)
                    else:
                        #print(f"Couldn't find a special situation for {match}.")
                        failure_count += 1
                else:
                    #print(f"{match} doesn't exist in root...")
                    failure_count += 1
            except Exception as e:
                #print(f"An error occured on {match}! Error: {e}")
                failure_count += 1
    if failure_count >= 50:
        #print(f"Reached {failure_count} errors! Please report this error in its entirety! {description}")
        return f"Reached {failure_count} errors! Please report this error in its entirety! {description}"
    else:
        #print(description)
        return description

print(main())