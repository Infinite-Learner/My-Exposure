import csv


class CSV:
    fn = ""

    def __int__(self):
        if "__name__" == "__main__":
            self.main()

    @staticmethod
    def file_open() -> object:
        fn = input("Enter Filename and Type (sample{Example.txt}) : ")
        try:
            file_ip = open("ItemsList/" + fn, 'x+', newline='')
        except FileExistsError:
            file_ip = open("ItemsList/" + fn, 'r+', newline='')
        return fn, file_ip

    @staticmethod
    def validate(file_ip):
        rec = []

        try:
            rec = next(csv.reader(file_ip))
            rec_val = len(rec)
            print(rec_val)
        except StopIteration:
            rec_val = 0
        return rec, rec_val

    @staticmethod
    def data_feed(file_ip, record, rec_val) -> None:
        print("Fields in Data_File", record, sep="\n")
        row = 1
        if rec_val != 0:
            row = rec_val // rec_val
        while True:
            data = []
            print(row, end='.')
            for i in record:
                data.append(input(f'Enter value for {i} : '))
            csv.writer(file_ip).writerow(data)
            row += 1
            if input("Type Stop to exit or Type Something to AddMore : ").capitalize() == "Stop":
                return file_ip

    @staticmethod
    def csv_write() -> None:
        fn, file = CSV.file_open()
        rc, rc_val = CSV.validate(file)
        if rc_val == 0:
            print("....No Field Found....\nInsert Some Data")
            print("Enter Field Names")
            col = list(input().strip().split(','))
            csv.writer(file).writerow(col)
            file.close()
        file = open("ItemsList/" + fn, 'r+', newline='')
        rc, rc_val = CSV.validate(file)
        CSV.data_feed(file, rc, rc_val)

    @staticmethod
    def main():
        CSV.csv_write()
