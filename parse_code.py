import json

with open('../../Downloads/core_music.ipynb', 'r') as f:
    print(''.join(json.load(f)["cells"][3]['source']))
