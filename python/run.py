from crawl import search
import os

warc_files_list = os.listdir("warc_data")

month_dict = {1:"1", 2:"2", 3:"3,4", 4:"5,6", 5:"7", 6:"8", 7:"9", 8:"10", 9:"11,12"}

for warc_file in warc_files_list:
    month = month_dict[int(warc_file[4])]
    warc_file_path = os.path.join("warc_data", warc_file)
    print(warc_file_path)
    with open(warc_file_path) as f:
        paths_list = f.readlines()
        for path in paths_list:
            path_final = path.replace("\n", "")
            search(path_final, month)