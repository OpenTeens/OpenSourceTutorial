import os
import hashlib
import json

all_tutorials = []
for folder in os.listdir("tutorial/src"):
    all_tutorials.extend(
        list(map(lambda x: f"{folder}/{x}", os.listdir(f"tutorial/src/{folder}")))
    )

tutorial_map = {}
for tutorial in all_tutorials:
    compiled_name = hashlib.md5(tutorial.encode()).hexdigest() + ".html"
    tutorial_map[tutorial] = compiled_name
    os.system(
        f"python lib/tutorial-maker/src/main.py -i tutorial/src/{tutorial} -o tutorial/build/{compiled_name} -a lib/tutorial-maker/src"
    )

json.dump(tutorial_map, open("tutorial/build/map.json", "w"))
