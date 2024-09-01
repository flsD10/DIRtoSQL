import os
import sqlite3
from datetime import datetime
#directory = input("Directory you would like to scan: ")
directory = "D:\\Coding\\dadproject\\hugeDatabaseProject\\test\\date"
#database = input("Enter the file path of the database: ")
database = "D:\\Coding\\dadproject\\hugeDatabaseProject\\test.db"
conn = sqlite3.connect(database)
cursor = conn.cursor()
date = datetime.today().strftime("%Y%m%d")
table = "CREATE TABLE " + "hello "+ "(FILE_NAME VARCHAR(255), ORIGINAL_SIZE FLOAT, COMPRESSED_SIZE FLOAT, BEST_IMAGE int);"
cursor.execute(table)

subdirectories = os.listdir(directory)

for subdirectory in subdirectories:
    newDirectory = directory + "\\" + subdirectory + "\\"
    files = os.listdir(newDirectory)
    for file in files:
        print(os.path.getsize(newDirectory + "\\" + file))
        cursor.execute("INSERT INTO " + "hello" + "(FILE_NAME, ORIGINAL_SIZE) VALUES (\'" + file + "\', " + str(round(os.path.getsize(newDirectory + "\\" + file)/ 1000,2)) + ")")

conn.commit()
conn.close()

