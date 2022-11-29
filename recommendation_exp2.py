import glob
import pandas as pd
import os



ono_cancel_list = [3,4,14,23,35,39]
riku_cancel_list = [9,15,23,32,38]

def datasetting(files, cancel_list):
    data_list = []
    joken_list = []
    # sub_exist_list = []
    # sub_dir_list = []
    for file in files:
        path, ext = os.path.splitext(file)
        file_name = path.split('/')[1]
        sub_exist = False
        sub_dir = None

        if not int(file_name) in cancel_list:
            action_time_list = []
            df = pd.read_csv(file,names=("time", "mousePos.x", "mousePos.Y", 
                                        "condition", "joken", "SajoAction",
                                        "SajoAnker", "MizuKukan", "MizuAction",
                                        "x", "goho", "autoactioncount", "Mizuhunmucount",
                                        "AutoHunmuLog", "carposition.z", "carsubposition.z",
                                        "fireposition.z", "firesubposition.z",
                                        "MizuGoOrStop","Input.GetMouseButton(0)",
                                        "Input.GetKeyDown(KeyCode.Return)"))
            print(file)
            num = df[df['joken'] > 0].head(1).index.values[0]
            start_num = df["time"].iat[num]
            joken = df["joken"].iat[num]

            carposition = df["carposition.z"].iat[num]
            position = ifif(carposition)
            carsubposition = df["carsubposition.z"].iat[num]
            if carsubposition < 0:
                subposition = ifif(carsubposition)
                sub_exist = True
                sub_dir = carposition - carsubposition 
                print("####")

            joken = str(file_name) + "_" + str(position) + "_" + str(sub_exist) + "_" + str(sub_dir)
            joken_list.append(joken)
            df = df[df['joken'] > 0]
            df["time"] = df["time"] - start_num
            df = df.reset_index(drop=True)
            action_count_list = df[df["autoactioncount"].diff() > 0].index.values
            for action_count in action_count_list:
                action_time_list.append(df["time"].iat[action_count])
            data_list.append(action_time_list)  
               
    final_df = pd.DataFrame(data_list).T
    final_df = final_df.set_axis(joken_list, axis = "columns")
    return final_df

def ifif(position):
    if position >= -40:
        posis = "1"
    elif position >-60:
        posis = "1,2"
    elif position >=-90:
        posis = "2"
    elif position >-110:
        posis = "2,3"
    elif position >=-140:
        posis = "3"
    elif position >-160:
        posis = "3,4"
    elif position >=-190:
        posis = "4"
    elif position >-210:
        posis = "4,5"
    elif position >=-240:
        posis = "5"
    elif position >-260:
        posis = "5,6"
    elif position >=-290:
        posis = "6"
    elif position >-310:
        posis = "6,7"
    elif position >=-340:
        posis = "7"
    elif position >-360:
        posis = "7,8"
    elif position >=-390:
        posis = "8"
    elif position >-410:
        posis = "8,9"
    elif position >=-440:
        posis = "9"
    elif position >-460:
        posis = "9,10"
    elif position >=-490:
        posis = "10"
    elif position >-510:
        posis = "10,11"
    elif position >=-540:
        posis = "11"
    elif position >-560:
        posis = "11,12"
    elif position >=-590:
        posis = "12"
    elif position >-610:
        posis = "12,13"
    elif position >=-640:
        posis = "13"
    elif position >-660:
        posis = "13,14"
    elif position >=-690:
        posis = "14"
    elif position >-710:
        posis = "14,15"
    elif position >=-740:
        posis = "15"
    elif position >-760:
        posis = "15,16"
    elif position >=-790:
        posis = "16"
    elif position >-810:
        posis = "16,17"
    elif position >=-840:
        posis = "17"
    elif position >-860:
        posis = "17,18"
    elif position >=-890:
        posis = "18"
    elif position >-910:
        posis = "18,19"
    elif position >=-940:
        posis = "19"
    elif position >-960:
        posis = "19,20"
    elif position >=-990:
        posis = "20"
    elif position >-1010:
        posis = "20,21"
    elif position >=-1040:
        posis = "21"
    elif position >-1060:
        posis = "21,22"
    elif position >=-1090:
        posis = "22"
    elif position >-1110:
        posis = "22,23"
    elif position >=-1140:
        posis = "23"
    elif position >-1160:
        posis = "23,24"
    elif position >=-1190:
        posis = "24"
    elif position >-1210:
        posis = "24,25"
    elif position >=-1240:
        posis = "25"
    elif position >-1260:
        posis = "25,26"
    elif position >=-1290:
        posis = "26"
    elif position >-1310:
        posis = "26,27"
    elif position >=-1340:
        posis = "27"
    elif position >-1360:
        posis = "27,28"
    elif position >=-1390:
        posis = "28"
    elif position >-1410:
        posis = "28,29"
    elif position >=-1440:
        posis = "29"
    elif position >-1460:
        posis = "29,30"
    elif position >=-1490:
        posis = "30"
    elif position >-1510:
        posis = "30,31"
    elif position >=-1540:
        posis = "31"
    elif position >-1560:
        posis = "31,32"
    elif position >=-1590:
        posis = "32"
    elif position >-1610:
        posis = "32,33"
    return posis


name_dict = {"riku2":riku_cancel_list, "mako2":ono_cancel_list}



if __name__ == '__main__':
    for name in name_dict.keys():
        files = glob.glob(name +'/*')
        final_df = datasetting(files, name_dict[name])
        final_df.to_csv("output_recommend_exp2/" + name + '_recomendation_exp2.csv')
