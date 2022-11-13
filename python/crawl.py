from warcio.archiveiterator import ArchiveIterator
import re
import requests
import sys
import csv

def search(path):
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

        # print(record.rec_headers.get_header("WARC-Target-URI"))
        uri = record.rec_headers.get_header("WARC-Target-URI")
        # if not ".com/" in record.rec_headers.get_header(
        #     "WARC-Target-URI"
        # ):
        if not ".com/" in uri:
            continue

        entries += 1
        contents = (
            record.content_stream()
            .read()
            .decode("utf-8", "replace")
        )

        contents_lower = contents.lower()

        if "covid" in contents_lower:
            # import pdb; pdb.set_trace()
            for keyword in keywords:
                if keyword in contents_lower:
                    print(keyword)
                    # import pdb; pdb.set_trace()
                    matching_entries += 1
                    uri_list.append([uri])
                    break

        # m = regex.search(contents)

        # if (m):
        #     import pdb; pdb.set_trace()

        # if m:
        #     matching_entries = matching_entries + 1
        #     hits = hits + 1
        #     m = regex.search(contents, m.end())

            # if (m):
            #     import pdb; pdb.set_trace()

        # while m:
        #     m = regex.search(contents, m.end())
        #     hits = hits + 1

    with open('uri.csv', 'a') as f:
        write = csv.writer(f)
        write.writerows(uri_list)

    print(
        "Python: "
        + "Matching entries:"
        + str(matching_entries)
        + "/"
        + str(entries)
    )
