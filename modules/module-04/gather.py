#!/usr/bin/env python3

import os
import exif
import shutil
from pathlib import Path

for root, dirs, files in os.walk('/home/ed/Data/govdocs1'):
    for file in files:
        path = Path(root) / Path(file)
        if path.suffix.lower() in ['.jpeg', '.jpg', '.png', '.gif']:
            try:
                print(path)
                img = exif.Image(path)
                if img.has_exif:
                    shutil.copy(path, Path('data/images') / path.name)
            except:
                pass


