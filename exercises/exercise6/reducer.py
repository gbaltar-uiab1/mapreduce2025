import sys
total_absoluto = 0.0
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) == 2:
        try:
            total_absoluto += float(data[1])
        except ValueError:
            continue

print "Total absoluto de vendas:\t%.2f" % total_absoluto
