# Single-Table SQL Quiz PY4E

### 1. Structured Query Language (SQL) is used to (check all that apply)
- [x] Insert data
- [x] Delete data
- [ ] Check Python code for erros
- [x] Create a table

### 2. Which of these is the right syntax to make a new table?
- [ ] MAKE people; 
- [ ] MAKE DATASET people;
- [ ] CREATE people;
- [x] CREATE TABLE people;

### 3. Which SQL command is used to insert a new row into a table?
- [ ] ADD ROW 
- [ ] INSERT ROW
- [x] INSERT INTO
- [ ] INSERT AFTER 

### 4. Which command is used to retrieve all records from a table?   
- [ ] RETRIEVE all FROM User
- [x] SELECT * FROM Users
- [ ] SELECT all FROM Users
- [ ] RETRIEVE * FROM Users 

### 5. Which keyword will cause the results of the query to be displayed in sorted order?
- [ ] GROUP BY 
- [x] ORDER BY
- [ ] WHERE
- [ ] None of these

### 6. In database terminology, another word for table is
- [ ] attribute
- [ ] field
- [ ] row
- [x] relation

### 7. In a typical online production environment, who has direct access to the production database?
- [x] Database Administrator
- [ ] Developer
- [ ] Project Manager
- [ ] UI/UX Designer

### 8. Which of the following is the database used in this class?
- [ ] Postgres
- [x] SQLite
- [ ] SQL Server
- [ ] MySQL
- [ ] Oracle

### 9. What happens if a DELETE command is run on a table without a WHERE clause?
- [ ] All the rows without a primary key will be deleted
- [ ] The first row in the table will be deleted
- [x] All rows in the table are deleted
- [ ] It is a syntax error

### 10. Which of the following commands would update a column named "name" in a table named "Users"?
- [ ] Users.name='new name'WHERE ...
- [ ] UPDATE Users (names) VALUES ('new name') WHERE ...
- [ ] Users->name='new name'WHERE...
- [x] UPDATE Users SET name='new name' WHERE... 

### 11. What does this SQL command do?
```
SELECT COUNT(*) FROM Users
```
- [ ] It is a syntax error 
- [x] It counts the rows in the table Users
- [ ] It only retrieves the rows of Users if there are at least two rows
- [ ] It adds a COUNT column to the Users table
