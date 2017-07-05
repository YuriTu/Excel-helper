#!/usr/bin/python
# Filename: using_sys.py

import os
import time

source = ["/Users/renren/0.temp","/Users/renren/1.qiang.tu/wex"]
target_dir = "/Users/renren/8.backup/"
# target = target_dir + time.strftime("%Y-%m-%d-%H-%M-%S") + ".zip"

today = target_dir + time.strftime("%Y-%m-%d")
now = time.strftime("%H-%M-%S")

comment = raw_input("Enter a comment ->")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"


# if not os.path.exists(today):
#     os.mkdir(today)
#     print("create dir")

target = today + os.sep + now + ".zip"
zip_command = "zip -qr %s %s" % (target, " ".join(source))


if os.system(zip_command) == 0:
    print("it's ok back up to %s" % target)
else:
    print("error")