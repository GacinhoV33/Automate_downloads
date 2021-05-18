import os
import time
import datetime
import pathlib
import xlrd
from shutil import copy


ext_list = [".txt", ".png", ".jpg", ".doc", ".pdf", ".bmp", ".csv", ".jpeg"]
images_ext = [".png", ".jpg", ".jpeg", ".bmp"]
doc_ext = [".doc", ".pdf", ".csv"]


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
    for filename in [f for f in os.listdir(initial_path) if "." in f]:
        if ".txt" in filename:
            modification_time = datetime.datetime.fromtimestamp(
                pathlib.Path(initial_path + "/" + filename).stat().st_ctime).date()

            new_name = filename
            while flag:
                if filename in os.listdir(initial_path + "/txt_files"):
                    new_name = "(1)" + new_name
                else:
                    flag = False
            if not os.path.exists(initial_path + "/txt_files/" + str(modification_time)):
                os.makedirs(initial_path + "/txt_files/" + str(modification_time))
            os.rename(os.path.join(initial_path, filename),
                      os.path.join(initial_path, "txt_files", str(modification_time), new_name))


def search_file_by_ext(ext: str, init_path: str, dest_path: str, days, start_time, end_time, lecture_names, flag=True):
    for filename in [f for f in os.listdir(init_path) if "." in f]:  # find better solution for "."
        if filename.endswith(ext):
            modification_time = datetime.datetime.fromtimestamp(
                pathlib.Path(init_path + "/" + filename).stat().st_ctime)
            file_day = modification_time.date().weekday()
            file_time = modification_time.time()
            lect_name = None
            for day in days:
                if file_day == day:
                    for s_time, e_time, name in zip(start_time, end_time, lecture_names):
                        if s_time < file_time < e_time:
                            lect_name = name

            new_filename = filename
            if lect_name:
                if ext in images_ext:
                    if not os.path.exists(dest_path + "/" + lect_name + "/images/" + str(modification_time.date())):
                        os.makedirs(dest_path + "/" + lect_name + "/images/" + str(modification_time.date()))

                    copy(init_path + "/" + filename,
                         dest_path + "/" + lect_name + "/images/" + str(modification_time.date()))
                elif ext in doc_ext:
                    if not os.path.exists(dest_path + "/" + lect_name + "/documents/" + str(modification_time.date())):
                        os.makedirs(dest_path + "/" + lect_name + "/documents/" + str(modification_time.date()))
                    copy(init_path + "/" + filename,
                         dest_path + "/" + lect_name + "/documents/" + str(modification_time.date()))
                else:
                    if not os.path.exists(
                            dest_path + "/" + lect_name + "/" + ext[1:] + "_files/" + str(modification_time.date())):
                        os.makedirs(
                            dest_path + "/" + lect_name + "/" + ext[1:] + "_files/" + str(modification_time.date()))
                    while flag:
                        if new_filename in os.listdir(dest_path + "/" + lect_name + "/" + ext[1:] + "_files/" + str(
                                modification_time.date())):
                            new_filename = "(1)" + new_filename
                        else:
                            flag = False
                    copy(init_path + "/" + filename,
                         dest_path + "/" + lect_name + "/" + ext[1:] + "_files/" + str(modification_time.date()))


def segregating_lectures():
    lectures_data = xlrd.open_workbook("Data.xls")
    arkusz_lectures = lectures_data.sheet_by_name(
        lectures_data.sheet_names()[0])  # choosing correct sheet from csv file
    lectures_names = list()
    start_time = list()
    end_time = list()
    days = list()
    n_rows = arkusz_lectures.nrows
    init_path1 = arkusz_lectures.row_values(1)[5]  # init_path is path of folder where files are downloaded
    # usually it's downloads or folder in documents where screenshots appeared
    init_path2 = arkusz_lectures.row_values(2)[5]
    dest_path = arkusz_lectures.row_values(1)[6]  # dest_path is destination where you want store data

    for i in range(1, n_rows):
        # Lectures
        lectures_names.append(arkusz_lectures.row_values(i)[0])

        # Time start
        data_values = xlrd.xldate_as_datetime(float(arkusz_lectures.row_values(i)[1]),
                                              lectures_data.datemode)  # the time conversation
        # is necessary, otherwise you will receive wrong format of time
        start_time.append(data_values.time())

        # Time end
        data_values = xlrd.xldate_as_datetime(float(arkusz_lectures.row_values(i)[2]), lectures_data.datemode)
        end_time.append(data_values.time())

        # Days
        days.append(arkusz_lectures.row_values(i)[3])

    # list of extensions that you wanna copy/sort

    for ext in ext_list:
        search_file_by_ext(ext, init_path1, dest_path, days, start_time, end_time, lectures_names, n_rows)
        search_file_by_ext(ext, init_path2, dest_path, days, start_time, end_time, lectures_names, n_rows)


segregating_lectures()

# try:
#     while True:
#         segregating_lectures()
# except:
#     raise RuntimeError("Some undefinied actions occured")

