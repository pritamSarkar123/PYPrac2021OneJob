import os
import shutil

print(os.name) #nt
print(os.getcwd()) #C:\Users\pritam\Desktop\pyPracforJob\Os
try:
	os.mkdir(os.path.join(os.path.dirname(__file__),"emptyDir"),mode=0o666) # dir created
	os.makedirs(os.path.join(os.path.dirname(__file__),"a\\b\\c"),mode=0o666) # hierarchy created
except FileExistsError:
	print(FileExistsError)
finally:
	os.rmdir(os.path.join(os.path.dirname(__file__),"emptyDir")) #dir deleted
	shutil.rmtree(os.path.join(os.path.dirname(__file__),"a")) # hierarchy deleted


# other functions like

# os.remove("file path ")

# import shutil
# shutil.rmtree("non empty dir path")

# os.chdir("../") going to prev dir
# etc available in net