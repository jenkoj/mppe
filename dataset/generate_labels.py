from functools import cmp_to_key
import pathlib
from os import walk,rename
import subprocess


#define paths
path = str(pathlib.Path().resolve())+"/stls_opt/"
path_log = str(pathlib.Path().resolve())+"/../output/"
path_slicer = '/Applications/Ultimaker\ Cura.app/Contents/MacOS/'

#get list of filenames 
filenames = next(walk(path), (None, None, []))[2]  # [] if no file


def get_cost(supports):
    cmd = ['./CuraEngine slice -v  -j settings.def.json -s support_enable="'+supports+'" -s center_object="true" -g -e0  -e0 -l /Users/jakob/Documents/mag/MPPE/dataset/stls_opt/'+filename+' -o /Users/jakob/Documents/mag/MPPE/gcode/test.gcode']    

    process = subprocess.Popen(cmd,shell=True,stdout = subprocess.PIPE,stderr=subprocess.PIPE,cwd="/Applications/Ultimaker Cura.app/Contents/MacOS")
    output,error = process.communicate()
    time = 0
    filament = 0
    #print(error.decode("utf-8"))
    for line in error.decode("utf-8").split("\n"):

        if 'Print time (s):' in line:
            time = int(line.split(":")[1])
        if 'Filament (mm^3):' in line:
            filament = int(line.split(":")[1])

    return time,filament    

c = 0
for filename in filenames:

    print("calculating times for file: ",filename.replace(".","_").split("_")[0],"****************************************************")

    print("calculating 1. time")
    time_no_supports, filament_no_supports = get_cost("false")
    print(time_no_supports,"s",filament_no_supports,"mm3")
    print("calculating 2. time")
    time_supports, filament_supports = get_cost("true")
    print(time_supports,"s",filament_supports,"mm3")
    rename(path+filename,path+filename.replace(".","_").split("_")[0]+"_"+str(time_no_supports)+"_"+str(filament_no_supports)+"_"+str(time_supports)+"_"+str(filament_supports)+".stl")
    print(filename,"->",path+filename.replace(".","_").split("_")[0]+"_"+str(time_no_supports)+"_"+str(filament_no_supports)+"_"+str(time_supports)+"_"+str(filament_supports))
    print("done!","*************************************************************************************")
    
    c = c+1



