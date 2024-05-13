import pyodbc

# Establish connection
conn = pyodbc.connect('DSN=sahil_dbms;UID=root;PWD=sahil')
cursor = conn.cursor()

# 8. Find society names in which more than five students have enrolled
query_8 = "SELECT SocName FROM SOCIETY s INNER JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY SocName HAVING COUNT(*) > 5;"
cursor.execute(query_8)
print("\nQuery 8 Results:")
for row in cursor.fetchall():
    print(row[0])
    
# Close connection
cursor.close()
conn.close()


