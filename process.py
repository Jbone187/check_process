import subprocess
import re
import sys


proc = subprocess.check_output(['ps', 'aux'])

decData = proc.decode("utf8")


if len(sys.argv) > 1:
    string = re.findall(sys.argv[1], decData)
    print(string)
else:
    print("Please Add Argument")
