# Many-to-Many Relationships and Python Quiz PY4E

### 1. How do we model many-to-many relationships between two database tables? 
- [ ] We use the ARRAY column type in both of the tables
- [ ] We add a table with two foreign keys
- [ ] We add 10 foreign keys to each table with names like artict_id, artist_id2, etc
- [ ] We use a BLOB column in both tables

### 2. In Python, what is a database "cursor" most like?
- [ ] A method within a class
- [ ] A function
- [ ] A Python dictionary
- [x] A file handle

### 3. What method do you call in SQLite cursor object in Python to run an SQL command?
- [ ] socket()
- [x] execute()
- [ ] run()
- [ ] send()

### 4. In the following SQL,
```
cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
```
### what is the purpose of the "?"?
- [x] It is a placeholder for the contents of the "org" variable
- [ ] It is a search wildcard
- [ ] It is a syntax error
- [ ] It allows more than one boolean operation in the WHERE clause

### 5. In the following Python code sequence (assuming cur is a SQLite cursor object),
```
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()
```
### what is the value if now rows match the WHERE clause?
- [x] None
- [ ] An empty list
- [ ] An empty dictionary
- [ ] -1

### 6. What does the LIMIT clause in the following SQL accomplish?
```
SELECT org, count FROM Counts
    ORDER BY count DESC LIMIT 10
```
- [x] It only retrieves the first 10 rows from the table
- [ ] It only sorts on the first 10 characters of the column
- [ ] It reverses the sort order if there are more than 10 rows
- [ ] It avoids reading data from any table other than counts

### 7. What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?
- [x] It allows multiple SQL statements separated by semicolons
- [ ] It allows database tables to be created
- [ ] It allows embedded Python to be executed
- [ ] It allows embedded JavaScript to be executed

### 8. What is the purpose of "OR IGNORE" in the following SQL:
```
INSERT OR IGNORE INTO Course (title) VALUES ( ? )
```
- [x] It makes sure tha if a particular title is already in the table, there are no duplicate rows inserted
- [ ] It ignores errors in the SQL syntax for the statement
- [ ] It updates the created_at value if the title already exists in the table
- [ ] It ignores any foreign key constraint errors

### 9. What do we generally avoid in many-to-many junction table?
- [ ] An AUTOINCREMENT primary key column
- [ ] A logical key
- [x] Two foreign keys
- [ ] Data items specific to the many-to-many relationship