from typing import List, Any
import re

links: List[Any]

with open("links.txt", 'r') as file:
    links = file.read().splitlines()

target_filename = links[0].split()[2]
dir_structure = links[1].split()[2]
organization_name = links[2].split()[2] + '/'

with open(target_filename, 'w') as target_file:
    target_file.flush()

for link in links[3:]:
    regex = r'(https://github.com/' + organization_name + ')'
    _dir = re.sub(regex, "", link)
    repo = re.sub(regex, "git@github.com:" + organization_name, link) + ".git"
    result = dir_structure + _dir + "," + repo
    print(result)
    with open(target_filename, 'a') as target_file:
        target_file.write(result + "\n")
