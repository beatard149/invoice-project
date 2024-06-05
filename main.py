import camelot as cam
import csv
import pandas as pd
table=cam.read_pdf("A1 Program test.docx (1).pdf",pages='1')
first_table=table[0]
# writing to csv file
with open("test.csv", 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(first_table.df)
table.export('A1 Program test.docx (1).csv', compress=True)

table[0].to_csv('A1 Program test.docx (1).csv')
print(table[0].df)