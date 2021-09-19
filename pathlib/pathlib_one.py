# youtube :-
# https://www.youtube.com/watch?v=DOgjN7RmHds

import pathlib 
import time

# path to the current script
path = pathlib.Path(__file__)
# print(path) =>
# g:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib\pathlib_one.py


# windows specific
windows_path = pathlib.WindowsPath(__file__) # IO operations present here
windows_pure_path = pathlib.PureWindowsPath(__file__) # IO operations not present here
# print(issubclass(pathlib.WindowsPath , pathlib.PureWindowsPath))  => True


# parts 
parts = windows_path.parts

# print(parts)
# ('g:\\', 'Full_backup', 'desktop_files_21_08_2021_back_up', 'pyPracforJob', 'pathlib', 'pathlib_one.py')

path = pathlib.Path(__file__)
#print(path.parts)
# ('g:\\', 'Full_backup', 'desktop_files_21_08_2021_back_up', 'pyPracforJob', 'pathlib', 'pathlib_one.py')

# base directory of the script
# print(path.parent) 
# OR
# print(path.parents[0]) # path.parents is an iterator
# g:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib

# print(path.parent.parent) ==
# print(path.parents[1]) ==
# g:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob

# join path

# path of a file in same directory as this script
new_file_path = pathlib.Path(__file__).parents[0].joinpath("abc.txt")
# print(new_file_path)
# g:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib\abc.txt

# create the file here
# new_file_path.touch(exist_ok=True) # if exist overwrite
# new_file_path.touch(exist_ok=False) # if exist raise error

################ recurssive delete #################
def del_directory(path):
    for sub in path.iterdir():
        if sub.is_dir():
            del_directory(sub)
        else:
            sub.unlink()
    path.rmdir()


def create_folder_file_and_delete_one():
    # create a directory if not exist then 
    # create file in it overwrite allowed
    # sleep for 5 sec and 
    # delete that folder again
    folder_path = pathlib.Path(__file__).parents[0].joinpath("Data")
    if not folder_path.exists():
        folder_path.mkdir()
    folder_path.joinpath("abc.txt").touch()
    time.sleep(5)
    # folder_path.rmdir()
    del_directory(folder_path)
    
# create_folder_file_and_delete_one()


def some_property_check():
    folder_path = pathlib.Path(__file__).parents[0].joinpath("Data")
    if not folder_path.exists():
        folder_path.mkdir()
    folder_path.joinpath("abc.txt").touch()
    folder_path.joinpath("abc.csv").touch()
    folder_path.joinpath("abc.json").touch()
    folder_path.joinpath("abc.xml").touch()
    
    for file_obj in pathlib.Path(__file__).parent.iterdir():
        print("+"*80)
        print(file_obj)
        print("Are you a directory? " + str(file_obj.is_dir()))
        print("Are you a file? " + str(file_obj.is_file()))
        print("Are you a symbolic link? " + str(file_obj.is_symlink()))
        # print("Are you a relative of the `Data` Folder? " + str(file_obj.is_relative_to(folder_path.parent)))
        print("File Drive is: " + str(file_obj.drive))
        print("File Stem is: " + str(file_obj.stem))
        print("File Anchor is: " + str(file_obj.anchor))
        print("File Name is: " + str(file_obj.name))
        print("File Suffix is: " + str(file_obj.suffix))
    
    time.sleep(5)
    del_directory(folder_path)
    
# some_property_check()



# current working directory 
# print(pathlib.Path.cwd())
# g:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib


# system home directory
# print(pathlib.Path.home())
# C:\Users\prita

# relative and absolute path
# print(pathlib.Path('pathlib_one.py'))
# pathlib_one.py
# print(pathlib.Path('pathlib_one.py').absolute())
# g:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib\pathlib_one.py

# resolve one # fill in the blanks
# print(pathlib.Path().resolve("g:/../pathlib_one.py"))
# G:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib

# resolve two # system wise path conversion
# print(pathlib.Path().resolve("G:/Full_backup/desktop_files_21_08_2021_back_up/pyPracforJob/pathlib"))
# G:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pathlib


# different Stats
# print(pathlib.Path(__file__).stat().st_size) # 4332
# print(pathlib.Path(__file__).stat().st_atime) # S1632045678.974753
# print(dir(pathlib.Path(__file__).stat()))
# ['__add__', '__class__', '__contains__',
# '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__', 
# '__lt__', '__module__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'count', 'index', 'n_fields', 'n_sequence_fields', 'n_unnamed_fields', 
# 'st_atime', 'st_atime_ns', 'st_ctime', 'st_ctime_ns', 'st_dev', 
# 'st_file_attributes', 'st_gid', 'st_ino', 'st_mode', 'st_mtime',
# 'st_mtime_ns', 'st_nlink', 'st_reparse_tag', 'st_size', 'st_uid']