import sys
import os
from datetime import datetime
import re
import glob

sys.path.insert(0, ".")
sys.path.insert(1, "..")

from corkus import __version__

copyright = datetime.today().strftime("%Y, MrBartusek")
exclude_patterns = ["_build"]
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints"
]
html_static_path = ["_static"]
html_theme = 'furo'
htmlhelp_basename = "Corkus.py"
intersphinx_mapping = {"python": ("https://docs.python.org", None)}
master_doc = "index"
nitpicky = True
project = "Corkus.py"
pygments_style = "sphinx"
release = __version__
source_suffix = ".rst"
suppress_warnings = ["image.nonlocal_uri"]
version = ".".join(__version__.split(".", 2)[:2])
autodoc_member_order = "bysource"
autodoc_typehints = "none"
autoclass_content = "class"
html_logo = "_static/logo.png"
autodoc_class_signature = "separated"
set_type_checking_flag = True

def to_camel_case(string):
    string = string.replace("UUID", "Uuid")
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

corkus_objects = []
with open('../corkus/objects/__init__.py', 'r') as objects:
    search = re.findall(r'(?m)^(?:from[ ]+(\S+)[ ]+)?import[ ]+([\S, ]+)[ ]*$', objects.read())
    for result in search:
        for item in result[1].split(", "):
            if item not in (
                "CorkusBase",
                "PartialBase"
            ):
                corkus_objects.append(item)

for f in glob.glob('code_overview/objects/*'):
    os.remove(f)

corkus_objects = sorted(corkus_objects)

for obj in corkus_objects:
    with open("code_overview/objects/" + to_camel_case(obj) + ".rst", "w") as f:
        f.write(".." + "\n")
        f.write("   This file is auto-generated" + "\n")
        f.write("\n")
        f.write(".. py:currentmodule:: corkus.objects" + "\n")
        f.write("\n")
        f.write(obj + "\n")
        f.write("=" * len(obj) + "\n")
        if obj.startswith("Partial"):
            f.write(".. include:: ../partial_object.rst" + "\n")
            f.write("\n")
        f.write(".. autoclass:: " + obj + "\n")
        f.write("   :inherited-members:" + "\n")
        if obj != "CorkusUUID":
            f.write("   :undoc-members:" + "\n")

with open("code_overview/corkus_objects.rst", "w") as f:
    f.write(".." + "\n")
    f.write("   This file is auto-generated" + "\n")
    f.write("\n")
    f.write("Working with Corkus Objects" + "\n")
    f.write("==========================="+ "\n")
    f.write("\n")
    f.write(".. toctree::" + "\n")
    f.write("   :maxdepth: 2" + "\n")
    f.write("   :caption: Objects" + "\n")
    f.write("\n")
    for obj in corkus_objects:
        f.write("   objects/" + to_camel_case(obj) + "\n")

def autodoc_skip_member(app, what, name, obj, skip, options):
    exclusions = ('__init__')
    exclude = name in exclusions
    return True if exclude else None

def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
