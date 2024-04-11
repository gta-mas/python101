# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("C:\\Users\\Gabo\\Desktop\\test.txt","C:\\Users\\Gabo\\Desktop\\copy.txt")       # 2 arguments; source (src), destination (dst)