#!/usr/bin/python
import sys

maxSale = 0.0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    
    # Ensure thisSale is treated as a number immediately
    try:
        thisSale = float(thisSale)
    except ValueError:
        continue

    if oldKey and oldKey != thisKey:
        print(oldKey + "\t" + str(maxSale))
        # Reset to 0.0 for the next store
        maxSale = 0.0

    oldKey = thisKey
    
    # Check for the maximum
    if thisSale > maxSale:
        maxSale = thisSale

# Output the final store
if oldKey is not None:
    print(oldKey + "\t" + str(maxSale))

