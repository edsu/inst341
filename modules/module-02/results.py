#!/usr/bin/env python3

import sys
import zipfile

username = sys.argv[1]

z = zipfile.ZipFile('data/{}.zip'.format(username))

total = 0
largest = None

for info in z.infolist():
    print(info.filename, info.file_size)
    total = total + info.file_size
    if largest is None or info.file_size > largest['size']:
        largest = {"name": info.filename, "size": info.file_size}

print('')
print('username:', username)
print('total:', total)
print('largest', largest)
print('')

