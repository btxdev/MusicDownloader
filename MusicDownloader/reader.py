import csv
from pathlib import Path

def searching_all_files(directory):
    file_list = []

    for x in directory.iterdir():
        if x.is_file():
            file_list.append(x)
        else:
            file_list.append(searching_all_files(directory/x))

    return file_list

def read_csv_file(path, names=None):
    if names is None:
        names = []
    with open(path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        first_row_ignored = False
        for row in csv_reader:
            if not first_row_ignored:
                first_row_ignored = True
                continue
            
            name = '{} - {}'.format(row[3], row[1])
            names.append(name)

    return names

def read_csv_files_in_directory(path, names=None):
    if names is None:
        names = []
    files = searching_all_files(path)
    for file in files:
        names = read_csv_file(file, names)
    return names

def read_txt_file(path, names=None):
    if names is None:
        names = []
    with open(path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            names.append(line)
    return names

def read_txt_files_in_directory(path, names=None):
    if names is None:
        names = []
    files = searching_all_files(path)
    for file in files:
        names = read_txt_file(file, names)
    return names