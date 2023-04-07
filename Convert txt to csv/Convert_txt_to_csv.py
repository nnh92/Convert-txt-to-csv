import os
import pandas as pd

src = "C:\\1"
file = [os.path.join(src,f) for f in os.listdir(src)]
print(file)

Vy_list = []
for file_i in file:
    if '.lst' in file_i:
        # dir
        print(file_i)
        # Excel sheet name
        sheetName = file_i[len(file_i)-12:len(file_i)-4]

        f = open(file_i, 'r')
        f = f.read().split("\n")

        Excel_dir = os.makedirs(src + "\Data_excel", exist_ok= True)

        # Find data value, delete unnecessary data
        for fi in f:
            if fi == "       No        VX        VY        VZ     PHI-X     PHI-Y     PHI-Z":
                f = f[f.index(fi)+2:]

        # Choose Node, Vy
        new_lst = []
        for fi in f:
            new_lst.append([fi.split()[0], fi.split()[2]])

        # Add new data to Vy_list
        if Vy_list == []:
            Vy_list = new_lst
        else:
            for i in Vy_list:
                i.append(new_lst[Vy_list.index(i)][1])

# Export data to excel
#print(Vy_list)
df_data = pd.DataFrame(Vy_list)
path = 'C:\\1\Data_excel\Data.xlsx'
df_data.to_excel(path)
print("Da xuat DL thanh cong")