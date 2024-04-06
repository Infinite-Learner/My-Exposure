import csv
def file_open():
    try:
        file = open("Data\\Data.csv",'r+',newline='')                                    
    except (FileNotFoundError):
        file = open("Data\\Data.csv",'w+',newline='')
    return file
def valid_check(file):
    global  rc1
    try:
            rc = []
            rc = next(csv.reader(file))
            rc1 = len(rc)
    except (StopIteration):
            rc1 = 0
    return rc,rc1
def data_feed(file,rc):
    n=1
    while(n==1):
        for i in rc:
            data = list(input(f'Enter {i} : ').strip().split(','))
        csv.writer(file).writerow(data)
file = file_open()
rc,rc1=valid_check(file)
if(rc1 == 0):
    print("....No Data Found....\nInsert Some Data")
    print("Enter Feild Names")
    col = list(input().strip().split(','))
    csv.writer(file).writerow(col)
    data_feed(file,rc)
if(rc1!=0):
    data_feed(file,rc)
