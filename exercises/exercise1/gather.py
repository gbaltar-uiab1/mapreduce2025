#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess

logfile = "TEST2.txt"
hdfs_dir_name="TEST2"
cat_to_txt = "hdfs dfs -cat {0}/* >{1}".format(hdfs_dir_name, logfile)

status = subprocess.call(cat_to_txt, shell=True)
print(status)
