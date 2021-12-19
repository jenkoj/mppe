import pathlib
from os import walk,rename
import subprocess


path_log = str(pathlib.Path().resolve())+"/../output/"

with open(path_log+'test', 'r') as f:
    for line in f.readlines():
        if 'Print time (s):' in line:
            time = print(int(line.split(":")[1]))
        if 'Filament (mm^3):' in line:
            print(int(line.split(":")[1]))