
t = 1603
path = r"D:\1. Project\Design data\res-" + str(t) + ".lst"
t1 = 1603-1
path1 = r"D:\1. Project\Design data\res-" + str(t1) + ".lst"

f = open(path, "r").readlines()
f1 = open(path1, "a+")

#print(f.read())

#print(type(f))

GetValue = False

for lst_i in range(len(f)):

    if f[lst_i].split() != []:

        if str(f[lst_i].split()[0]) == "RESULTS" and str(f[lst_i].split()[2]) == "NODE" and str(f[lst_i].split()[3]) == "DISPLACEMENT":
            lst_start = lst_i + 3

for lst_i in range(lst_start,len(f)):

    if f[lst_i].split() != []:
        #for i in range(len(f[lst_i].split()[0])):
        #    f1.write(str(f[lst_i].split()[i]))

        f1.writelines(f[lst_i].split())
        
            #print(str(f[lst_i].split()))