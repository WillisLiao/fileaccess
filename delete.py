import os
for i in range(1, 30):
    foldName = "char{}.txt".format(i)
    if os.path.exists(foldName):
        os.rmdir(foldName)
        print(f"folder {foldName} has been deleted!!")
    else:
        print(f"{foldName} folder is not existed!")
print('Done!')
