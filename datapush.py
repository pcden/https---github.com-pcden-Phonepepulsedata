import csv
import mysql.connector
import os
#d
# Database connection details
db_host = 'localhost'
db_user = 'root'
db_password = 'Denjerry&7'
db_name = 'phonepepulse'
h = '3306'

# giving directory name
dirname = 'D:\Dimpu\ProjectWorks\Python\PhonepePulseData\Data'
 
# giving file extension
ext = ('.csv')
 
# iterating over all files
for files in os.listdir(dirname):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
   

        # Specify the target table name in your database
        table_name = os.path.splitext(files)[0]
        # CSV file path
        csv_file_path = 'D:/Dimpu/ProjectWorks/Python/PhonepePulseData/Data'

        csv_file_path = csv_file_path + '/' +files

        # Establish database connection
        conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name, port=h)

        #   Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Read CSV file and insert data into the database
        with open(csv_file_path, 'r') as csv_file:
         csv_reader = csv.reader(csv_file)
         header = next(csv_reader)  # Read the header to get column names

         # Create the SQL query with placeholders for column names
         columns = ', '.join(header)
         placeholders = ', '.join(['%s'] * len(header))
         insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Loop through the rows in the CSV and execute the insert query
         for row in csv_reader:
            cursor.execute(insert_query, row)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()
    else:
        continue