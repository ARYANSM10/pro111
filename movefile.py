import time
import os 
import shutil 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/user/Downloads"
to_dir="C:/Users/user/Desktop"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)