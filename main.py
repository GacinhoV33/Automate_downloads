import watchdog.observers
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import datetime
import pathlib

#
# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         for filename in os.listdir(folder_name):
#             src = folder_name + "/" + filename
#             if ".txt" in filename:
#                 new_destination = folder_destination_txt + "/" + filename
#                 if filename in os.listdir(folder_destination_txt):
#                     new_destination += "_"
#                 os.rename(src, new_destination)
#
#             elif ".png" or ".jpg" or ".bmp" in filename:
#                 new_destination = folder_destination_png + "/" + filename
#                 if filename in os.listdir(folder_destination_png):
#                     new_destination[-5:] += "_.jpg"
#                 os.rename(src, new_destination)
#             elif ".pdf" or ".doc" or ".csv" in filename:
#                 new_destination = folder_destination_pdfdoccsv + "/" + filename
#                 os.rename(src, new_destination)
#             # else:
#             #     new_destination = folder_destination_rest + "/" + filename


def check_path_folders(path):
    if not os.path.exists(path + "/txt_files"):
        os.makedirs(path + "/txt_files")
    if not os.path.exists(path + "/images_files"):
        os.makedirs(path + "/images_files")
    if not os.path.exists(path + "/pdf_doc_files"):
        os.makedirs(path + "/pdf_doc_files")
    if not os.path.exists(path + "/rar_files"):
        os.makedirs(path + "/rar_files")


def sort_files(initial_path: str, flag=True):
    check_path_folders(initial_path)
    # print([f for f in os.listdir(initial_path)])
    for filename in [f for f in os.listdir(initial_path) if "." in f]:
        if ".txt" in filename:
            modification_time = datetime.datetime.fromtimestamp(pathlib.Path(initial_path + "/" + filename).stat().st_ctime).date()

            new_name = filename
            while flag:
                if filename in os.listdir(initial_path + "/txt_files"):
                    new_name = "(1)" + new_name
                else:
                    flag = False
            if not os.path.exists(initial_path + "/txt_files/" + str(modification_time)):
                os.makedirs(initial_path + "/txt_files/" + str(modification_time))
            # os.rename(initial_path + "/" + filename, initial_path + "/txt_files/" + str(modification_time) + "/" +new_name)
            os.rename(os.path.join(initial_path, filename), os.path.join(initial_path, "txt_files", str(modification_time), new_name))


sort_files("C:/Users/gacek/Desktop/Projekty IT/Python")
#

# def create_name_folders():
#     pass
#
#
# def swap_folders(initial_path:str, destination_path:str):
#
#     if not
#         create_name_folders()

# sort_files("C:/Users/gacek/Downloads/txt_files")



#for downloads
# folder_name2 = "C:/Users/gacek/Downloads"
# folder_destination_txt = "
# folder_destination_png = "C:/Users/gacek/Downloads/images_files"
# folder_destination_rest = "C:/Users/gacek/Downloads/rest"
# folder_destination_pdfdoccsv = "C:/Users/gacek/Downloads/pdf"
# event_handler = MyHandler()
# observer = watchdog.observers.Observer()
# observer.schedule(event_handler, folder_name2, recursive=True)
# observer.start()






# # some folder from computer
# folder_name = "C:/Users/gacek/Desktop/Projekty IT/Python/initial"
# folder_destination_txt = "C:/Users/gacek/Desktop/Projekty IT/Python/txt_files"
# folder_destination_png = "C:/Users/gacek/Desktop/Projekty IT/Python/images_files"
# folder_destination_rest = "C:/Users/gacek/Desktop/Projekty IT/Python/rest"
# folder_destination_pdfdoccsv = "C:/Users/gacek/Desktop/Projekty IT/Python/pdf"
# event_handler = MyHandler()
# observer = watchdog.observers.Observer()
# observer.schedule(event_handler, folder_name, recursive=True)
# observer.start()
#
# try:
#     while True:
#         time.sleep(10)
# except KeyboardInterrupt:
#     observer.stop()
#
# observer.join()
