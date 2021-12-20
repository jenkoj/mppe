import pathlib
import stltovoxel
from os import walk


#get list of filenames 
path = str(pathlib.Path().resolve())+"/stls_opt/"
path_save = str(pathlib.Path().resolve())+"/voxelsFloat/"
filenames = next(walk(path), (None, None, []))[2]  # [] if no file
filenames_save = next(walk(path_save), (None, None, []))[2]  # [] if no file


#broken 
#filenames_to_ignore = ["168","130","151","161","124","5","147","32","13","8","69","68","169","66","48","47","186","42","41","3","38","25","27"]
filenames_to_ignore = ["169"]
#for filenname in list(reversed(filenames)):
for filenname in filenames:
	
	print("starting ",filenname)
	
	if filenname.split(".")[0]+".npy" in filenames_save or filenname.split("_")[0] in filenames_to_ignore:
		print("exists")
	else:
		stltovoxel.convert_file('stls_opt/'+filenname, 'voxelsFloat/'+filenname.split(".")[0]+'.npy')
        
#your_mesh = mesh.Mesh.from_file('04_Motor_Bracket_DD_RH.stl')
#mesh  = read_ply('04_Motor_Bracket_DD_RH.stl')
# input=r"04_Motor_Bracket_DD_RH.stl"
# output=r"voxels/test.svx"
# resolution = 50 #Resolution, into how many layers the model should be divided
# stltovoxel.convert_file(input, output, resolution)

#voxelize(mesh, 300, solid=True)