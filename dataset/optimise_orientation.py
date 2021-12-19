import pathlib
from os import walk,rename
import subprocess


path = str(pathlib.Path().resolve())+"/stls/"

#get list of filenames 
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

c = 0
for filename in filenames:
    bashCommand = "python3 ../Tweaker-3/Tweaker.py -i stls/"+filename+" -o stls_opt/"+str(c)+".stl -min sur -x"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(c,filename,output,error)
    
    c = c+1



#code to rename all files in folder 
# for filename in filenames:
#     #bashCommand = "python3 ../Tweaker-3/Tweaker.py -i stls"+filename+" -o stls_opt/"+str(c)+".stl -min sur -x"
#     #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#     #output, error = process.communicate()
#     #print(c,filenames[1])#,output,error)

#     #
#     rename(path+filename,path+str(c)+"_non_opt.stl")
#     print(filename,"->",str(c)+"_non_opt.stl")
#     c = c+1