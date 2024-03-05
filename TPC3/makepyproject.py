import jinja2
from glob import glob
from pathlib import Path
import json

modes = glob("*.py")
if len(modes) > 1:
    if modes[0] != 'make_pyproject.py':
        name = modes[0].replace(".py","")
    else:
        name = modes[1].replace(".py","")
else:
    name = input("Module: ")

metaPath = str(Path.home()) + "/metadata.json"

try:
    with open(metaPath, 'r') as meta:
        metadata = json.load(meta)
        author = metadata['author']
        email = metadata['email']

except FileNotFoundError:
    author = input('Author: ')
    email = input('Email: ')

pyVer = input('Python Version: ')

#TODO: fazer opçao automatica 

depend = []
d = int(input("How many dependencies?: "))

for n in range(0,d):
    depend.append(input(f'''Insert dependency {n+1}: '''))

pp = jinja2.Template('''
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{author}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">={{pyVer}}"
dynamic = ["version", "description"]
dependencies = {{depend}}

[project.scripts]
{{name}} = "{{name}}:main"
''')

r = pp.render({"name":name,"author":author,"email":email, "pyVer":pyVer, "depend":depend})

with open("pyproject.toml","w") as file:
    file.write(r)