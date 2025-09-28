#!/usr/bin/env python3
import json
import os
from pathlib import Path

scriptpath = os.path.dirname(os.path.realpath(__file__))
diction = ""
if Path(scriptpath + "/cedict_ts.u8").exists():
    diction = open(scriptpath + "/cedict_ts.u8", "rt").read().split('\n')
limit = 5

with open(scriptpath + '/cedict-cfg.json', 'rt') as cfg:
    cfg_data = json.load(cfg)
    limit = cfg_data["limit"]
    diction = open(cfg_data["dictionary_path"], "rt").read().split('\n')

while True:
    query = input("Type your search query or 'x' to cancel.\n")
    if query == "x":
        break
    else:
        count = 0
        for line in diction:
            if count == limit:
                break
            if query in line:
                count += 1
                print("\n" + line.strip("/"))
