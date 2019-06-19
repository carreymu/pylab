import csv
from collections import namedtuple

if __name__ == "__main__":
    print("============read csv============")
    with open("file/ppdac1.csv") as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        for row in f_csv:
            print(row[1])

    print("============read csv by rowname============")
    with open("file/ppdac1.csv") as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            rrow = Row(*r)
            print(rrow)

    print("============read csv by dict============")
    with open("file/ppdac1.csv") as f:
        fdict_csv = csv.DictReader(f)
        for row in fdict_csv:
            print("mb:{},val:{}".format(row['mobile'], row['value']))

    print("============write csv============")
    """
    'w'为擦写,'a+'为追加.
    """
    headers=['timestamp', 'mobile', 'value']
    rows = [{"timestamp":'2018-02-09 13:26:27', "mobile":'17799768504', "value":'2'}]
    with open('file/ppdac1.csv', 'a+') as f:
        f_csv = csv.DictWriter(f, headers)
        # f_csv.writeheader()
        f_csv.writerows(rows)