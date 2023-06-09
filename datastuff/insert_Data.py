import sqlite3, csv, os


# inserting the data into the database
curr_path = os.getcwd()
curr_data_path = os.path.join(curr_path,'CSVData')

#change the csv file name depending on which file you want to enter
with open(os.path.join(curr_data_path,'Publisher.csv'),'r') as f:
    readFile = csv.reader(f)

    connDB = sqlite3.connect(os.path.join(curr_path,'Database.db'))
    connectDB = connDB.cursor()

    for row in readFile:
        #change the table name, fields, VALUES, and rows depending on the table you want to enter
        connectDB.execute('INSERT INTO PUBLISHER (publisher_name,phone,address) VALUES (?,?,?)',(row[0],row[1],row[2]))

connDB.commit()
connDB.close()
