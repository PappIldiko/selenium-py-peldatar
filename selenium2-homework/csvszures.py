import csv

with open('table_in.csv', 'r', encoding="utf-8") as csvf:
    csvreader = csv.reader(csvf)
    with open('new_table_in.csv', "w", encoding="utf-8") as res_csv:
        table = csv.reader(csvf, delimiter=',')
        for row in table:
            res_csv.write(row[1] + ', ' + row[0] + '\n')
