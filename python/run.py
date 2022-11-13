from crawl import search
import os

warc_files_list = os.listdir("warc_data")

count = 0

for warc_file in warc_files_list:
    warc_file_path = os.path.join("warc_data", warc_file)
    print(warc_file_path)
    with open(warc_file_path) as f:
        paths_list = f.readlines()
        for path in paths_list:
            path_final = path.replace("\n", "")
            search(path_final)
            count += 1
            if count == 10:
                break