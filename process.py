import subprocess
import re
import sys


data = subprocess.check_output(['ps', 'aux'])

val = data.decode("utf8")


if len(sys.argv) > 1:
    string = re.findall(sys.argv[1], val)
    print(string)
else:
    print("Please Add Argument")
