import pyodbc

# Connect to the MySQL database using ODBC
conn = pyodbc.connect('DSN=sahil_dbms;UID=root;PWD=sahil')

# Create a cursor object to execute queries
cursor = conn.cursor()

# 1. Retrieve names of students enrolled in any society
query_1 = "SELECT s.StudentName FROM student s INNER JOIN ENROLLMENT e ON s.RollNo = e.RollNo;"
cursor.execute(query_1)
print("\nQuery 1 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 2. Retrieve all society names
query_2 = "SELECT SocName FROM SOCIETY;"
cursor.execute(query_2)
print("\nQuery 2 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 3. Retrieve students' names starting with letter ‘A’
query_3 = "SELECT StudentName FROM student WHERE StudentName LIKE 'A%';"
cursor.execute(query_3)
print("\nQuery 3 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 4. Retrieve students' details studying in courses ‘computer science’ or ‘chemistry’
query_4 = "SELECT * FROM student WHERE Course IN ('computer science', 'chemistry');"
cursor.execute(query_4)
print("\nQuery 4 Results:")
for row in cursor.fetchall():
    print(row)  

# 5. Retrieve students’ names whose roll no either starts with ‘X’ or ‘Z’ and ends with ‘9’
query_5 = "SELECT * FROM student WHERE (RollNo LIKE 'X%' OR RollNo LIKE 'Z%') AND RollNo LIKE '%9';"
cursor.execute(query_5)
print("\nQuery 5 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 6. Find society details with more than N TotalSeats where N is to be input by the user
N = input("Enter the value of N: ")
query_6 = f"SELECT * FROM SOCIETY WHERE TotalSeats > {N};"
cursor.execute(query_6)
print("\nQuery 6 Results:")
for row in cursor.fetchall():
    print(row)  

# 7. Update society table for mentor name of a specific society
MentorName = input("Enter the new mentor name: ")
SocID = input("Enter the Society ID: ")
query_7 = f"UPDATE SOCIETY SET MentorName = '{MentorName}' WHERE SocID = '{SocID}';"
cursor.execute(query_7)
conn.commit()

# Updated record
query_select = f"SELECT * FROM SOCIETY WHERE SocID = '{SocID}';"
cursor.execute(query_select)
updated_record = cursor.fetchone()
print("\nUpdated Record:")
print(updated_record)

# 8. Find society names in which more than five students have enrolled
query_8 = "SELECT SocName FROM SOCIETY s INNER JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY SocName HAVING COUNT(*) > 5;"
cursor.execute(query_8)
print("\nQuery 8 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 9. Find the name of youngest student enrolled in society ‘NSS’
query_9 = "SELECT StudentName FROM student WHERE RollNo IN (SELECT RollNo FROM ENROLLMENT WHERE SID = 'NSS') ORDER BY DOB ASC LIMIT 1;"
cursor.execute(query_9)
print("\nQuery 9 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 10. Find the name of most popular society (on the basis of enrolled students)
query_10 = "SELECT SocName FROM SOCIETY s INNER JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY SocName ORDER BY COUNT(*) DESC LIMIT 1;"
cursor.execute(query_10)
print("\nQuery 10 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 11. Find the name of two least popular societies (on the basis of enrolled students)
query_11 = "SELECT SocName FROM SOCIETY s INNER JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY SocName ORDER BY COUNT(*) ASC LIMIT 2;"
cursor.execute(query_11)
print("\nQuery 11 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 12. Find the student names who are not enrolled in any society
query_12 = "SELECT StudentName FROM student WHERE RollNo NOT IN (SELECT RollNo FROM ENROLLMENT);"
cursor.execute(query_12)
print("\nQuery 12 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 13. Find the student names enrolled in at least two societies
query_13 = "SELECT RollNo FROM ENROLLMENT GROUP BY RollNo HAVING COUNT(*) >= 2;"
cursor.execute(query_13)
print("\nQuery 13 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 14. Find society names in which maximum students are enrolled
query_14 = "SELECT SocName FROM SOCIETY s INNER JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY SocName ORDER BY COUNT(*) DESC LIMIT 1;"
cursor.execute(query_14)
print("\nQuery 14 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 15. Find names of all students who have enrolled in any society and society names in which at least one student has enrolled
query_15 = "SELECT StudentName FROM student WHERE RollNo IN (SELECT RollNo FROM ENROLLMENT);"
cursor.execute(query_15)
print("\nQuery 15 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 16. Find names of students who are enrolled in any of the three societies ‘Debating’, ‘Dancing’ and ‘Sashakt’.
query_16 = "SELECT StudentName FROM student WHERE RollNo IN (SELECT RollNo FROM ENROLLMENT WHERE SID IN ('Debating', 'Dancing', 'Sashakt'));"
cursor.execute(query_16)
print("\nQuery 16 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 17. Find society names such that its mentor has a name with ‘Gupta’ in it.
query_17 = "SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%';"
cursor.execute(query_17)
print("\nQuery 17 Results:")
for row in cursor.fetchall():
    print(row[0])  
# 18. Find the society names in which the number of enrolled students is only 10% of its capacity.
query_18 = "SELECT SocName FROM SOCIETY s INNER JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY SocName HAVING COUNT(*) = 0.1 * MAX(TotalSeats);"
cursor.execute(query_18)
print("\nQuery 18 Results:")
for row in cursor.fetchall():
    print(row[0])
# 19. Display the vacant seats for each society.
query_19 = "SELECT s.SocName, (s.TotalSeats - COUNT(e.RollNo)) AS VacantSeats FROM SOCIETY s LEFT JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY s.SocName, s.TotalSeats;"
cursor.execute(query_19)
print("\nQuery 19 Results:")
for row in cursor.fetchall():
    print(row[0], row[1])  

# 20. Increment Total Seats of each society by 10%
query_20 = "UPDATE SOCIETY SET TotalSeats = TotalSeats + CEILING(0.1 * TotalSeats);"
cursor.execute(query_20)
print("\nQuery 20 Results: Updated total seats by 10% successfully")

# 21. Add the enrollment fees paid ('Yes'/'No') field in the enrollment table.
query_21 = "ALTER TABLE ENROLLMENT ADD COLUMN EnrollmentFee VARCHAR(3);"
cursor.execute(query_21)
print("\nQuery 21 Results: Enrollment fees paid field added successfully")

# 22. Update date of enrollment of society id 's1' to '2018-01-15', 's2' to current date and 's3' to '2018-01-02'.
# Update date of enrollment for society id 's1' to '2018-01-15'
query_22_s1 = "UPDATE ENROLLMENT SET DateOfEnrollment = '2018-01-15' WHERE SID = 'ABC110';"
cursor.execute(query_22_s1)

# Update date of enrollment for society id 's2' to current date
query_22_s2 = "UPDATE ENROLLMENT SET DateOfEnrollment = CURDATE() WHERE SID = 'ABC103';"
cursor.execute(query_22_s2)

# Update date of enrollment for society id 's3' to '2018-01-02'
query_22_s3 = "UPDATE ENROLLMENT SET DateOfEnrollment = '2018-01-02' WHERE SID = 'ABC106';"
cursor.execute(query_22_s3)
conn.commit()

print("\nQuery 22 Results: Date of enrollment updated successfully")


# 23. Create a view to keep track of society names with the total number of students enrolled in it.
query_23 = "CREATE VIEW SocietyEnrollmentCount AS SELECT s.SocName, COUNT(e.RollNo) AS TotalEnrolled FROM SOCIETY s LEFT JOIN ENROLLMENT e ON s.SocID = e.SID GROUP BY s.SocName;"
cursor.execute(query_23)
print("\nQuery 23 Results: Society enrollment count view created successfully")

# 24. Find student names enrolled in all the societies.
query_24 = "SELECT RollNo FROM (SELECT RollNo, COUNT(DISTINCT SID) AS num_societies FROM ENROLLMENT GROUP BY RollNo) AS temp WHERE num_societies = (SELECT COUNT(DISTINCT SocID) FROM SOCIETY);"
cursor.execute(query_24)
print("\nQuery 24 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 25. Count the number of societies with more than 5 students enrolled in it
query_25 = "SELECT COUNT(*) FROM (SELECT DISTINCT SID FROM ENROLLMENT GROUP BY SID HAVING COUNT(*) > 5) AS tmp;"
cursor.execute(query_25)
print("\nQuery 25 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 26. Add column Mobile number in student table with default value '9999999999'
query_26 = "ALTER TABLE student ADD COLUMN MobileNumber VARCHAR(10) DEFAULT '9999999999';"
cursor.execute(query_26)
print("\nQuery 26 Results: Mobile number column added to student table successfully")

# 27. Find the total number of students whose age is > 20 years.
query_27 = "SELECT COUNT(*) FROM student WHERE DATEDIFF(CURRENT_DATE(), DOB) / 365.25 > 20;"
cursor.execute(query_27)
print("\nQuery 27 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 28. Find names of students who are born in 2001 and are enrolled in at least one society.
query_28 = "SELECT StudentName FROM student WHERE YEAR(DOB) = 2001 AND RollNo IN (SELECT RollNo FROM ENROLLMENT);"
cursor.execute(query_28)
print("\nQuery 28 Results:")
for row in cursor.fetchall():
    print(row[0]) 

# 29. Count all societies whose name starts with 'S' and ends with 't' and at least 5 students are enrolled in the society.
query_29 = "SELECT COUNT(*) FROM (SELECT SocName FROM SOCIETY WHERE SocName LIKE 'S%t' GROUP BY SocName HAVING COUNT(*) >= 5) AS tmp;"
cursor.execute(query_29)
print("\nQuery 29 Results:")
for row in cursor.fetchall():
    print(row[0])  

# 30. Display the following information: Society name, Mentor name, Total Capacity, Total Enrolled, Unfilled Seats
query_30 = "SELECT s.SocName, s.MentorName,s.TotalSeats,COUNT(e.RollNo) AS TotalEnrolled, s.TotalSeats - COUNT(e.RollNo) AS UnfilledSeats from society s LEFT join enrollment e ON s.SocID = e.SID GROUP BY s.SocName, s.MentorName, s.TotalSeats;"
cursor.execute(query_30)
print("\nQuery 30 Results:")
for row in cursor.fetchall():
    print(row)  

# Close the cursor and connection
cursor.close()
conn.close()
