import pypyodbc as odbc
import pandas as pd
from requests import head
"""
Step:1 Importing data set from csv
"""
df=pd.read_csv('C:/Users/shish/Desktop/TFQ/Dataset_n_Scripts/student_response.csv')
print(df)
df.columns
'''
Step 2: Specify Column
'''
columns = ['roll_number', 'question_paper_code', 'question_number',
       'option_marked']
df_data= df[columns]
records=df_data.values.tolist()
records[:10]
# Define the connection string to the SQL database
conn_str = 'DRIVER={SQL Server};SERVER=DESKTOP-2TPQOB3\SQLEXPRESS;DATABASE=ANSWER;'
# Create a connection object
conn = odbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Drop table if exists ST_RESP;CREATE TABLE ST_RESP (roll_number INTEGER, question_paper_code INTEGER, question_number INTEGER,option_marked NVARCHAR(10));")
'''
Step 3.2 Create a cursor connection
'''
sql_insert = '''
    INSERT INTO ST_RESP
    Values(?, ?, ?, ?)
'''
cursor.executemany(sql_insert,records)
cursor.commit()
cursor.close()
conn.close()