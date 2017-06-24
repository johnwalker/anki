#!/usr/bin/env python3
import os
from anki import Collection

def collectionPath():
    return os.path.join("/home/john/.local/share/Anki2/User 1", "collection.anki2")

def loadCollection():
    return Collection(collectionPath(), log=True)

if __name__ == '__main__':
    col = loadCollection()
