#!/usr/bin/python
import sys

# variables para a hora maior
max_val = 0.0
max_key = None

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    thisKey, thisSale = data_mapped
    
    if oldKey and oldKey != thisKey:
        if salesTotal > max_val:
            max_val = salesTotal
            max_key = oldKey
        
        oldKey = thisKey
        salesTotal = 0
    
    oldKey = thisKey
    salesTotal += float(thisSale)

# comprobar o grupo derradeiro perantes de rematar
if oldKey is not None and salesTotal > max_val:
    max_val = salesTotal
    max_key = oldKey

# print final co maximo global
if max_key is not None:
    print "{}\t{}".format(max_key, max_val)
