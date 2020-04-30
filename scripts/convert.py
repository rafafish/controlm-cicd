#! /usr/bin/env python3

import csv
import json
import sys

csvfile = open(sys.argv[1], 'r')
jsonfile = open('result.json', 'w')

fieldnames = ("id","seq","nome","estado","industria")
reader = csv.DictReader(csvfile, fieldnames)

firstline = True

for row in reader:
    if firstline: 
        jsonfile.write('[')
        json.dump(row, jsonfile)
        firstline = False
    else:
        jsonfile.write(',')
        json.dump(row, jsonfile)


jsonfile.write(']')