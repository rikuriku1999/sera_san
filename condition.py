import pandas as pd
import glob
import os



def exchenge_kukan(df):
    time_kukan = []
    kukan_list = []
    kukan = None
    for index,row in df.iterrows():
        if row.SajoAnker == 0 :
            if not row.MizuKukan in kukan_list:
                kukan_list.append(row.MizuKukan)
            beforeAnker = 0
            print(kukan_list)
        if row.SajoAnker == 1 :
            if beforeAnker == 1:
                if row.MizuAction == 2:
                    if row.MizuKukan in kukan_list:
                        kukan_list.remove(row.MizuKukan) #区間リストにあれば
                        print("#############################")
                if row.MizuAction == 1:
                    if not row.MizuKukan in kukan_list:
                        kukan_list.append(row.MizuKukan)
                        print("&&&&&&&&&&&&&&&&&&&&&&&&")
                kukan = ",".join(map(str,kukan_list))
            time_kukan.append([row.time,kukan])
            print(time_kukan)
            print("hogeeeeeee")
            beforeAnker = 1
    return time_kukan

if __name__ == "__main__" :
    files = glob.glob('output/*')
    for file in files:
        path, ext = os.path.splitext(file)
        file_name = path.split('/')[1]
        df = pd.read_csv(file)
        kukans = exchenge_kukan(df)
        kukans_df = pd.DataFrame(kukans, columns=["time", "kukan"])
        kukans_df.to_csv("output2/" + file_name + '_kukan.csv')
