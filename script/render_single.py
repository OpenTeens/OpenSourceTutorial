import json
import jinja2
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str, required=True)
args = parser.parse_args()

name = args.name
map_json = json.load(open("tutorial/build/map.json"))
html_path = f"tutorial/build/{map_json[name]}"


# parse map_json into tree-like dict
def parse_map_json(map_json):
    tree = {}
    for key, value in map_json.items():
        key = key.split("/")
        t = tree
        for k in key[:-1]:
            if k not in t:
                t[k] = {}
            t = t[k]
        t[key[-1]] = value

    return tree


tree = parse_map_json(map_json)

# cut tree
name = name.split("/")
if len(name) > 2:
    for i in range(0, len(name) - 2):
        tree = tree[name[i]]

nav_tree_html = ""


def render_nav_tree(tree, depth=0):
    global nav_tree_html
    for key, value in tree.items():
        class_name = "collapsed"
        if key == name[depth + 1]:
            class_name = "active"

        if type(value) == str:
            nav_tree_html += f"<li class='{class_name} url' onclick=\"goto_url('{value}')\">{key}</li>"
        else:
            nav_tree_html += (
                f"<li class='{class_name}' onclick='expand_navt(this)'>{key}<ul>"
            )
            render_nav_tree(value, depth + 1)
            nav_tree_html += "</ul></li>"


# print(tree)
render_nav_tree(tree)

# render html
with open(html_path) as f:
    article_html = f.read()

template = jinja2.Template(open("script/template/single_article.html").read())
html = template.render(
    article=article_html, nav_tree=nav_tree_html, title=name[-1].split(".")[0]
)

with open(html_path, "w") as f:
    f.write(html)
