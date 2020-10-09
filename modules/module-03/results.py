#!/usr/bin/env python3

# unzip student directories to a submissions directory
# run this ./results.py <username> to see the correct
# results to compare against the notebook results
# putting the submission notebooks in the submissions
# directory will mean they can easily load the data.

import sys
import puid
import magic
import pathlib
import collections

data = pathlib.Path("submissions/" + sys.argv[1])

magics = []
puids = []
for p in data.iterdir():
    magics.append(magic.from_file(p.as_posix()))
    puids.append(puid.get_puid(p))

print("magic")
for format, count in collections.Counter(magics).most_common(10):
    print("{0:3n} {1:s}".format(count, format))

print("")
print("puid")
for format, count in collections.Counter(puids).most_common(10):
    if format is None:
        format = "None"
    print("{0:3n} {1:s}".format(count, format))


