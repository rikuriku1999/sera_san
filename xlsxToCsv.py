import pandas as pd
import glob
import os

files = glob.glob('ono/*')
for file in files :
    path, ext = os.path.splitext(file)
    print(file)
    #filelist = path.split('\\')
    # name = filelist[5]
    # read_file = pd.read_excel (file)
    # read_file.to_csv ("ono_csv/" + name + ".csv", index = None, header=True)