#!/usr/bin/env python3 

# this script is used to create a random set of files and a
# checksum manifest.json for the files. the fixity for one
# of the files is incorrect

import os
import csv
import json
import random
import hashlib
import pathlib
import zipfile

from os.path import join, basename

# data collected from:
# http://downloads.digitalcorpora.org/corpora/files/govdocs1/

data_dir = '/home/ed/Data/govdocs1'
roster = '../../roster.csv'

# get the users
usernames = []
for row in csv.reader(open(roster)):
    parts = row[1].split('@')
    usernames.append(parts[0])
usernames.append('inst341')

# get the files
paths = []
for root, dirs, files in os.walk(data_dir):
    for name in files:
        p = os.path.join(root, name)
        if pathlib.Path(p).stat().st_size < 10000:
            paths.append(os.path.join(root, name))

def sha256(p):
    # not memory efficient, but ok for these purposes
    p = pathlib.Path(p)
    h = hashlib.sha256()
    with p.open('rb') as fh:
        h.update(fh.read())
    return h.hexdigest()

# write a zip file for each user

for user in usernames:
    zip_path = 'data/{}.zip'.format(user)
    z = zipfile.ZipFile(zip_path, 'w')
    manifest = []
    for p in random.sample(paths, 25):
        z.write(p, join(user, basename(p)))
        manifest.append({'path': p, 'sha256': sha256(p)})

    # flip a character in the checksum of a random entry in the manifest
    if user != 'inst341':
        e = manifest[random.randint(0, 24)]
        c = '0' if e['sha256'][0] != '0' else '1'
        e['sha256'] = c + e['sha256'][1:]

    open('manifest.json', 'w').write(json.dumps(manifest, indent=2))
    z.write('manifest.json', join(user, 'manifest.json'))
    z.close()
