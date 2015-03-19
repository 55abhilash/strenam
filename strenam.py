import os
for filename in os.listdir("place here the directory"):
	if filename.startswith("Place here the string"):
		os.rename(filename, filename[Place here how do you wish to rename]) #Eg. to rename "horizon" to "zon" it will be filename[4:]
	
