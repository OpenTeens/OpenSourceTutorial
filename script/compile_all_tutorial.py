import os
import hashlib
import json

all_tutorials = []
for root, dirs, files in os.walk("tutorial/src"):
    for file in files:
        if file.endswith(".md"):
            relative_path = os.path.relpath(f"{root}/{file}", "tutorial/src").replace("\\", "/")
            all_tutorials.append(relative_path)

tutorial_map = {}
for tutorial in all_tutorials:
    compiled_name = hashlib.md5(tutorial.encode()).hexdigest() + ".html"
    tutorial_map[tutorial] = compiled_name
    os.system(
        f"python lib/tutorial-maker/src/main.py -i \"tutorial/src/{tutorial}\" -o \"tutorial/build/{compiled_name}\" -a lib/tutorial-maker/src"
    )

json.dump(tutorial_map, open("tutorial/build/map.json", "w"))
