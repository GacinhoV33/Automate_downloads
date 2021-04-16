import watchdog.observers
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_name):
            src = folder_name + "/" + filename
            if ".txt" in filename:
                new_destination = folder_destination_txt + "/" + filename
                if filename in os.listdir(folder_destination_txt):
                    new_destination += "_"
                os.rename(src, new_destination)
            elif ".png" or ".jpg" or ".bmp" in filename:
                new_destination = folder_destination_png + "/" + filename
                if filename in os.listdir(folder_destination_png):
                    new_destination[-5:] += "_.jpg"
                os.rename(src, new_destination)
            elif ".pdf" or ".doc" or ".csv" in filename:
                new_destination = folder_destination_pdfdoccsv + "/" + filename
                os.rename(src, new_destination)
            # else:
            #     new_destination = folder_destination_rest + "/" + filename



#for downloads
# folder_name2 = "C:/Users/gacek/Downloads"
# folder_destination_txt = "C:/Users/gacek/Downloads/txt_files"
# folder_destination_png = "C:/Users/gacek/Downloads/images_files"
# folder_destination_rest = "C:/Users/gacek/Downloads/rest"
# folder_destination_pdfdoccsv = "C:/Users/gacek/Downloads/pdf"
# event_handler = MyHandler()
# observer = watchdog.observers.Observer()
# observer.schedule(event_handler, folder_name2, recursive=True)
# observer.start()






# some folder from computer
folder_name = "C:/Users/gacek/Desktop/Projekty IT/Python/initial"
folder_destination_txt = "C:/Users/gacek/Desktop/Projekty IT/Python/txt_files"
folder_destination_png = "C:/Users/gacek/Desktop/Projekty IT/Python/images_files"
folder_destination_rest = "C:/Users/gacek/Desktop/Projekty IT/Python/rest"
folder_destination_pdfdoccsv = "C:/Users/gacek/Desktop/Projekty IT/Python/pdf"
event_handler = MyHandler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, folder_name, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
