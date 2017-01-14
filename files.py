import os


root = 'Aus'

allFiles = []
dirDict = {}

for (dirpath, dirnames, filenames) in  os.walk(root):
    dirDict[os.path.basename(dirpath)] =  filenames;   


#print("Equivalent String : %s" % str (dirDict))

for key,value in dirDict.items():
    print("Dict key [%s], Value = %s" % (key, value)) 