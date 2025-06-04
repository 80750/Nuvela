import sqlite3
import csv
con = sqlite3.connect("jarvis.db")
cursor_obj = con.cursor()
#query = "DROP TABLE contacts "
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name varchar(100), path varchar(1000))"
cursor_obj.execute(query)
# query = "INSERT INTO sys_command VALUES(null, 'arduino ide', 'C:\\Program Files\\Arduino IDE\\Arduino IDE.exe')"
# cursor_obj.execute(query)
# con.commit()
# con.close()
#query = "INSERT INTO sys_command VALUES(null, 'spotify', 'https://apps.microsoft.com/detail/9NCBCSZSJRSB?hl=en-us&gl=US&ocid=pdpshare')"
#query = "DELETE FROM sys_command WHERE name = 'spotify'"
#cursor_obj.execute(query)
#con.commit()
#con.close()
#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name varchar(100), path varchar(1000))"
#cursor_obj.execute(query)
#cursor_obj.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
# desired_columns_indices = [0, 18]
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor_obj.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
# con.commit()
# con.close()
# query = "INSERT INTO contacts VALUES (null,'Pawan', '1234567890', 'null')"
# cursor_obj.execute(query)
# con.commit()
# query = 'pawan'
# query = query.strip().lower()

# cursor_obj.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor_obj.fetchall()
# print(results[0][0])