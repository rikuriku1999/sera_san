import glob
import pandas as pd
import os


ono_cancel_list = [42,51,57,59]
riku_cancel_list = [36,40,41,54]

features = ["SajoAnker","MizuKukan","MizuAction","goho","AutoHunmuLog"]
def datasetting(files,cancel_list,name):
    joken_list = []
    for file in files:
        path, ext = os.path.splitext(file)
        file_name = path.split('/')[1]
        if int(file_name) in cancel_list:
            df = pd.read_csv(file,names=("time", "mousePos.x", "mousePos.Y", 
                                        "condition", "joken", "SajoAction",
                                        "SajoAnker", "MizuKukan", "MizuAction",
                                        "x", "goho", "autoactioncount", "Mizuhunmucount",
                                        "AutoHunmuLog", "Input.GetMouseButton(0)",
                                        "Input.GetKeyDown(KeyCode.Return)"))
            num = df[df['joken'] > 1].head(1).index.values[0]
            start_num = df["time"].iat[num]
            joken = df["joken"].iat[num]
            joken_list.append(joken)
            df = df[df['joken'] > 1]
            df["time"] = df["time"] - start_num
            df = df.reset_index(drop=True)
            dff_list = []
            df = df[["time","SajoAnker","MizuKukan","MizuAction","goho","AutoHunmuLog"]]
            for feature in features:
                changed_values = df[abs(df[feature].diff()) > 0].index.values
                for value in changed_values:
                    if not value in dff_list:
                        dff_list.append(value)
            dff_list.sort()
            final_df = df.iloc[dff_list]
            toCsv(final_df,file_name ,joken,name)

def toCsv(df,file_name,joken,name):
    df.to_csv("output/" + name + str(file_name) + "-" + str(joken) + '.csv')


name_dict = {"stephanie":[i for i in range(100)], "riku":riku_cancel_list, "ono":ono_cancel_list}

if __name__ == '__main__':
    for name in name_dict.keys():
        files = glob.glob(name +'_csv/*')
        datasetting(files, name_dict[name], name)