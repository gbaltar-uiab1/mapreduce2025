#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess

# Greetings
print("\nLauncher started.\n")

# Check files are uploaded
# dummy: sales_data.txt

print("Checking remote filesystem...")
print("=" * 30)

files_needed = ['testsales.txt', 'salesdata.txt']
for f in files_needed:
    if subprocess.call(["hdfs", "dfs", "-test", "-e", f]) != 0:
        print("[ ERROR ]: File not found on HDFS: " + f)
	print("\nPlease upload file manually usingÂ\nhdfs dfs -put " + f)
        sys.exit(1)
    else:
        print("[ PASS ]: File " + f + " found. Continue...")



# Check remote folder doesn't exist
# dir_name = "COMPRASXTENDA_20M"

dir_name = "TEST2"
print("\nChecking remote filesystem...")
print("=" * 40)

if subprocess.call(["hdfs", "dfs", "-test", "-d", dir_name]) == 0:
    print("[ ERROR ]: Remote directory already exists.")
    print("Please remove directory using the following commands:")
    print(" hdfs dfs -rm <dir_name>/*")
    print(" hdfs dfs -rmdir <dir_name>")
    sys.exit(1)
else:
    print("[ PASS ]: Target directory available: " + dir_name)


# Launch mapred

print("\nExecuting mapred. Please wait...\n")

# mapred_command = "mapred streaming -files mapper.py,reducer.py,../files/testsales.txt   -input sales_data_20M_rows.txt   -output  COMPRASXTENDA_20M_2 -mapper "python mapper.py" -reducer "python reducer.py"

# string.format()

cmd = "mapred streaming -files {0},reducer.py,../files/testsales.txt -input {1} -output {2} -mapper 'python mapper.py' -reducer 'python reducer.py'".format("mapper.py", "sales_data_20M_rows.txt", dir_name)
status = subprocess.call(cmd, shell=True)

#if subprocess.call("mapred streaming -files ... -input ... -output ...", shell=True) == 0:
#    print("Success")



# Recoller o resultado de HDFS con cat e gardalo nun ficheiro de saida en local
cat_to_txt = "hdfs dfs -cat Â{0}/*.format(dir_name)
