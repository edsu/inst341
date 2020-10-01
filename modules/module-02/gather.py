#!/usr/bin/env python3 

# this script is used to create a random set of files per student
# for them to use in their notebook assignment

import os
import csv
import random
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

usernames = ['edsu']

# get the files
paths = []
for root, dirs, files in os.walk(data_dir):
    for name in files:
        p = os.path.join(root, name)
        if pathlib.Path(p).stat().st_size < 10000:
            paths.append(os.path.join(root, name))

# write a zip file for each user

for user in usernames:
    zip_path = 'data/{}.zip'.format(user)
    z = zipfile.ZipFile(zip_path, 'w')
    for p in random.sample(paths, 25):
        z.write(p, join(user, basename(p)))
    z.close()
