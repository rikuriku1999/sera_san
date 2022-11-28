import glob
import pandas as pd
import os



ono_cancel_list = [42,51,57,59]
riku_cancel_list = [36,40,41,54]

def datasetting(files, cancel_list):
    data_list = []
    joken_list = []
    for file in files:
        path, ext = os.path.splitext(file)
        file_name = path.split('/')[1]

        if not int(file_name) in cancel_list:
            action_time_list = []
            df = pd.read_csv(file,names=("time", "mousePos.x", "mousePos.Y", 
                                        "condition", "joken", "SajoAction",
                                        "SajoAnker", "MizuKukan", "MizuAction",
                                        "x", "goho", "autoactioncount", "Mizuhunmucount",
                                        "AutoHunmuLog", "Input.GetMouseButton(0)",
                                        "Input.GetKeyDown(KeyCode.Return)"))
            print(file)
            num = df[df['joken'] > 1].head(1).index.values[0]
            start_num = df["time"].iat[num]
            joken = df["joken"].iat[num]
            joken = str(file_name) + "_" + str(joken)
            joken_list.append(joken)
            df = df[df['joken'] > 1]
            df["time"] = df["time"] - start_num
            df = df.reset_index(drop=True)
            action_count_list = df[df["autoactioncount"].diff() > 0].index.values
            for action_count in action_count_list:
                action_time_list.append(df["time"].iat[action_count])
            data_list.append(action_time_list)  
               
    final_df = pd.DataFrame(data_list).T
    final_df = final_df.set_axis(joken_list, axis = "columns")
    return final_df

name_dict = {"riku":riku_cancel_list, "ono":ono_cancel_list}



if __name__ == '__main__':
    for name in name_dict.keys():
        files = glob.glob(name +'_csv/*')
        final_df = datasetting(files, name_dict[name])
        final_df.to_csv("output_recommend/" + name + '_recomendation.csv')
