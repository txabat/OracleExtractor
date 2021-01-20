import csv
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_18_5")
con = cx_Oracle.connect('username/passwd@server/sid')

filename="data_file_name"
dirtmp="../export/tmp/"
filetmp=dirtmp+filename+".tmp"
dirout="../export/"
fileout=dirout+filename+".csv"

query = """SELECT col1, col2, col3
FROM table"""

cursor = con.cursor()
csv_file = open(filetmp, "w")
# writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC) only quote for non-numeric fields
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_ALL)
# writer.writerow(["column_name_1", "column_name_2", "column_name_3"...]) replace column_name_x by the column real name.

r = cursor.execute(query)
for row in cursor:
    writer.writerow(row)

cursor.close()
con.close()
csv_file.close()
  
s = open(filetmp, mode='r', encoding='ansi').read()
open(fileout, mode='w', encoding='utf-8-sig').write(s)
