# CSV files : comma separated values 

# name , age , job , salary 
# sairam , 29 , trainer , 50000 

# csv methods 

# writer()
# writerow()
# writerows()
# reader()
# Dictwriter()
# Dictreader()


import csv

with open("data.csv","w" ,newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name " , "age " , "salary"])
    writer.writerow(["Rocky " , 29 , 50000])


import csv

data =[["sairam",26,40000],["sumit",22,30000],["chiru", 60,1000000]]

with open("data.csv","a") as f:
    writer = csv.writer(f)
    writer.writerows(data)

import csv

with open("data.csv","r") as f:
    reader = csv.reader(f)
   
    for row in reader:
        print(row)