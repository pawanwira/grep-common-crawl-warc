from warcio.archiveiterator import ArchiveIterator
import re
import requests
import sys
import csv

def search(path, month):
    entries = 0
    matching_entries = 0
    uri_list = []

    keywords = ["economic impact", "economy", "economic", "economics"]

    import pdb; pdb.set_trace()
    prefix = "https://data.commoncrawl.org/"
    file_name = prefix + path

    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    stream = None

    if file_name.startswith("http://") or file_name.startswith(
        "https://"
    ):
        stream = requests.get(file_name, stream=True).raw
    else:
        stream = open(file_name, "rb")

    for record in ArchiveIterator(stream):
        if record.rec_type == "warcinfo":
            continue

        uri = record.rec_headers.get_header("WARC-Target-URI")
        if not ".com/" in uri:
            continue

        entries += 1

        if "covid" in uri:
            matching_entries += 1
            uri_list.append([uri, month])

        # contents = (
        #     record.content_stream()
        #     .read()
        #     .decode("utf-8", "replace")
        # )

        # contents_lower = contents.lower()

        # if (contents_lower.count("covid") > 10):
        #     for keyword in keywords:
        #         if keyword in contents_lower:
        #             print(keyword)
        #             matching_entries += 1
        #             uri_list.append([uri, month])
        #             break

    with open('url.csv', 'a') as f:
        write = csv.writer(f)
        write.writerows(uri_list)

    print(
        "Python: "
        + "Matching entries:"
        + str(matching_entries)
        + "/"
        + str(entries)
    )
