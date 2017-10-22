import os

folder = '/Users/snarang/music'

for root, dirs, filenames in os.walk(folder):
    for f in msuic:
        log = open(os.path.join(root, f), 'r')
        print(f)
