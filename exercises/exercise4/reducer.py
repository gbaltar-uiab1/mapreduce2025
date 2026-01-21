import sys

max_key, max_val = None, 0
current_key, current_sum = None, 0

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t')
        count = int(count)

        if key == current_key:
            current_sum += count
        else:
            if current_key and current_sum > max_val:
                max_val, max_key = current_sum, current_key
            current_key, current_sum = key, count
    except:
        continue

if current_sum > max_val:
    max_val, max_key = current_sum, current_key

if max_key:
    # Corrixido: pechado o parentese do .format()
    print "{}\t{}".format(max_key, max_val)
