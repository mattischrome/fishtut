# Python script / zsh script to move files around

# for each file in the directory
#   + 

# Save at root of fishtut repo

import os
import re
from pathlib import Path
posts_dir = './content/posts/'

date_search = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}-')

for filename in os.scandir(posts_dir):
    if (filename.path.endswith(".markdown") and filename.is_file()):
        new_file = date_search.sub('',filename.path,1)
        new_dir = new_file.replace(".markdown",'')
        new_path = new_file.replace(".markdown", "/index.md")
        print(new_file)
        print(new_dir)
        print(new_path)
        os.mkdir(new_dir)
        Path(filename.path).rename(new_path)