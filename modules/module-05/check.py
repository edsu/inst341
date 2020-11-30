#!/usr/bin/env python3

import sys
import json
import hashlib

from pathlib import Path

user = sys.argv[1]
submissions = Path('submissions')
manifest_file = submissions / user / 'manifest.json'
manifest = json.load(manifest_file.open())

def get_sha256(p):
    data = p.open('rb').read()
    h = hashlib.sha256(data)
    return h.hexdigest()

for entry in manifest:
    p = submissions / entry['path']
    sha256 = get_sha256(p)
    found_sha256 = get_sha256(p)
    if entry['sha256'] != found_sha256:
        print(p, 'should be', sha256, 'but found', found_sha256)
