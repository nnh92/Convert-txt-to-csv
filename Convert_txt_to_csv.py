import os
import pandas as pd

src = "C:\\1"
file = [os.path.join(src,f) for f in os.listdir(src)]
print(file)

for file_i in file:
    if '.lst' in file_i:
        #dir
        print(file_i)
        # Excel sheet name
        sheetName = file_i[len(file_i)-12:len(file_i)-4]

        f = open(file_i, 'r')
        f = f.read().split("\n")

        Excel_dir = os.makedirs(src + "\Data_excel", exist_ok= True)

        for fi in f:
            if fi == "       No        VX        VY        VZ     PHI-X     PHI-Y     PHI-Z":
                f = f[f.index(fi)+2:]

        lst = []
        for fi in f:
            lst.append(fi.split())
            #print(lst)
            df_data = pd.DataFrame(lst)
            path = 'C:\\1\Data_excel\Data.xlsx'
            writer = pd.ExcelWriter(path , engine = 'openpyxl', mode= 'a')
            df_data.to_excel(writer, sheet_name= sheetName)

        writer.close()
        print("Da xuat DL thanh cong")