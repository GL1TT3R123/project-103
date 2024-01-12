import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/user/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hi,{event.src_path} has been created")
    def on_deleted(self,event):
        print(f"hi,{event.src_path} has been deleted")
    def on_modified(self,event):
        print(f"hi,{event.src_path} someone has modified")    
    def on_moved (self,event):
        print(f"hi,someone moved {event.src_path} to {event.dest_path}") 

eventHandler = FileEventHandler()    

observer = Observer()
observer.schedule(eventHandler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stop")  
    observer.stop() 