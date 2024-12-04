# open関数

import os
path = "38_file_operation/test.txt"

greeting = open(path)

print(greeting.read())

greeting.close()