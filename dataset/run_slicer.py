#from functools import cmp_to_key
# import pathlib
# from os import walk,rename
# import subprocess

# cmd = ['./CuraEngine slice -v  -j settings.def.json -s support_enable="true" -s center_object="true" -g -e0  -e0 -l /Users/jakob/Documents/mag/MPPE/dataset/stls_opt/1.stl -o /Users/jakob/Documents/mag/MPPE/gcode/test.gcode']    
# process = subprocess.Popen(cmd,shell=True,stdout = subprocess.PIPE,stderr=subprocess.PIPE,cwd="/Applications/Ultimaker Cura.app/Contents/MacOS")
# output,error = process.communicate()

# for line in error.decode("utf-8").split("\n"):

#     if 'Print time (s):' in line:
#         time = int(line.split(":")[1])
#         print(time)
#     if 'Filament (mm^3):' in line:
#         filament = int(line.split(":")[1])
#         print(filament)


f = "1.stl"

print(f.replace(".","_"))